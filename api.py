import requests

class GitHubAPI:
    def __init__(self, token):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def _make_request(self, method, url, params=None, json=None):
        try:
            response = requests.request(method, url, headers=self.headers, params=params, json=json)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def get_user_repos(self, username):
        url = f"{self.base_url}/users/{username}/repos"
        params = {"sort": "stars", "direction": "asc", "per_page": 50}
        return self._make_request("GET", url, params=params)

    def get_repo_issues(self, owner, repo_name, state="open", per_page=40):
        url = f"{self.base_url}/repos/{owner}/{repo_name}/issues"
        params = {"state": state, "per_page": per_page}
        return self._make_request("GET", url, params=params)

    def create_issue(self, owner, repo_name, title, body):
        url = f"{self.base_url}/repos/{owner}/{repo_name}/issues"
        payload = {"title": title, "body": body}
        return self._make_request("POST", url, json=payload)

    def get_issue_body(self, owner, repo_name, issue_number):
        url = f"{self.base_url}/repos/{owner}/{repo_name}/issues/{issue_number}"
        return self._make_request("GET", url)
