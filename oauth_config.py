#configuration file that reads in the environment variables set in the shell and contains the predefined URLs that Google uses for its identity provider endpoints.

import os
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
redirect_callback = os.environ.get('REDIRECT_CALLBACK')
authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
token_url = 'https://accounts.google.com/o/oauth2/token'
