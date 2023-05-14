import requests

# GitHub API endpoint for creating repositories
url = 'https://api.github.com/user/repos'

# GitHub username and access token
username = input('your_username: ')
access_token =input('your_access_token: ')

# Repository name and description
repository_name =input('my-new-repo: ')
repository_description = 'This is a new repository created with Python'

# Request payload to create the repository
repository_payload = {
    'name': repository_name,
    'description': repository_description,
    'private': False  # Set to True for a private repository
}

# Set authentication headers
headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Send the POST request to create the repository
response = requests.post(url, json=repository_payload, headers=headers)

# Check the response status code
if response.status_code == 201:
    print(f'Repository "{repository_name}" created successfully.')

    # Retrieve the repository details from the response
    repository_details = response.json()

    # Repository details
    owner = repository_details['owner']['login']
    repo = repository_details['name']

    # Path and name of the README.md file
    path = 'README.md'

    # Content of the README.md file
    readme_content = '# My Project\n\nThis is a description of my project.'

    # Request payload to create or update the README.md file
    readme_payload = {
        'path': path,
        'message': 'Create or update README.md',
        'content': readme_content
    }

    # Format the URL with repository details
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'

    # Send the PUT request to create or update the README.md file
    readme_response = requests.put(url, json=readme_payload, headers=headers)

    # Check the response status code for the README.md creation or update
    if readme_response.status_code == 201:
        print(f'{path} created or updated successfully.')
    else:
        print('Failed to create or update the README.md file.')
        print(f'Response status code: {readme_response.status_code}')
        print(f'Response body: {readme_response.text}')

else:
    print('Failed to create the repository.')
    print(f'Response status code: {response.status_code}')
    print(f'Response body: {response.text}')
