import os
import re
import json
import requests

def run_query(query, headers):
    request = requests.post("https://api.github.com/graphql", json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query failed with status code {request.status_code}. {json.dumps(request.json(), indent=2)}")

def subscribe_to_issues_and_prs(owner, repo, keywords):
    headers = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
    search_query = f"repo:{owner}/{repo} is:open {' '.join('"' + keyword + '"' for keyword in keywords)}"
    query = f"""
    {{
      search(query: "{search_query}", type: ISSUE, first: 100) {{
        edges {{
          node {{
            ... on Issue {{
              id
              title
            }}
            ... on PullRequest {{
              id
              title
            }}
          }}
        }}
      }}
    }}
    """

    result = run_query(query, headers)
    for edge in result["data"]["search"]["edges"]:
        node = edge["node"]
        node_id = node["id"]

        mutation = f"""
        mutation {{
          updateSubscription(input: {{subscribableId: "{node_id}", state: SUBSCRIBED}}) {{
            clientMutationId
          }}
        }}
        """
        run_query(mutation, headers)

if __name__ == "__main__":
    owner = "yourusername"
    repo = "yourrepository"
    keywords = ["OADP", "backup"]

    subscribe_to_issues_and_prs(owner, repo, keywords)
