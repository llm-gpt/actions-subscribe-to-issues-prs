# actions-subscribe-to-issues-prs

## Prompt 1

GHA workflow to on a schedule subscribe to issues and pull request in a repository containing word "OADP" or "backup"

## Response 1

<div class="relative flex w-[calc(100%-50px)] flex-col gap-1 md:gap-3 lg:w-[calc(100%-115px)]"><div class="flex flex-grow flex-col gap-3"><div class="min-h-[20px] flex flex-col items-start gap-4 whitespace-pre-wrap"><div class="markdown prose w-full break-words dark:prose-invert light"><p>To set up a GitHub Actions (GHA) workflow that runs on a schedule and subscribes to issues and pull requests containing the words "OADP" or "backup" in a repository, you can follow these steps:</p><ol><li><p>Create a new file in your repository under the <code>.github/workflows</code> directory. Name it something like <code>subscribe_to_issues_and_prs.yml</code>.</p></li><li><p>In this YAML file, define a scheduled workflow using the <code>on</code> key with a <code>schedule</code> event, and provide a cron syntax to define how often you want the workflow to run. For example, if you want it to run daily at 00:00 UTC, you would use:</p></li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>yaml</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-yaml"><span class="hljs-attr">on:</span>
  <span class="hljs-attr">schedule:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">cron:</span> <span class="hljs-string">'0 0 * * *'</span>
</code></div></div></pre><ol start="3"><li>Define the workflow steps, including setting up the environment with the necessary language and tools (e.g., Python and the PyGithub library) and running a script that subscribes to the desired issues and PRs:</li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>yaml</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-yaml"><span class="hljs-attr">name:</span> <span class="hljs-string">Subscribe</span> <span class="hljs-string">to</span> <span class="hljs-string">Issues</span> <span class="hljs-string">and</span> <span class="hljs-string">PRs</span>

<span class="hljs-attr">on:</span>
  <span class="hljs-attr">schedule:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">cron:</span> <span class="hljs-string">'0 0 * * *'</span>

<span class="hljs-attr">jobs:</span>
  <span class="hljs-attr">subscribe:</span>
    <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>

    <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Set</span> <span class="hljs-string">up</span> <span class="hljs-string">Python</span>
      <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/setup-python@v2</span>
      <span class="hljs-attr">with:</span>
        <span class="hljs-attr">python-version:</span> <span class="hljs-number">3.9</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Install</span> <span class="hljs-string">dependencies</span>
      <span class="hljs-attr">run:</span> <span class="hljs-string">|
        python -m pip install --upgrade pip
        pip install PyGithub
</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Check</span> <span class="hljs-string">issues</span> <span class="hljs-string">and</span> <span class="hljs-string">PRs</span>
      <span class="hljs-attr">env:</span>
        <span class="hljs-attr">GITHUB_TOKEN:</span> <span class="hljs-string">${{</span> <span class="hljs-string">secrets.GITHUB_TOKEN</span> <span class="hljs-string">}}</span>
      <span class="hljs-attr">run:</span> <span class="hljs-string">|
        python .github/scripts/subscribe_to_issues_and_prs.py
</span></code></div></div></pre><ol start="4"><li>In the <code>.github/scripts</code> directory of your repository, create a Python script named <code>subscribe_to_issues_and_prs.py</code>:</li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python"><span class="hljs-keyword">import</span> os
<span class="hljs-keyword">import</span> re
<span class="hljs-keyword">from</span> github <span class="hljs-keyword">import</span> Github

<span class="hljs-keyword">def</span> <span class="hljs-title function_">subscribe_to_issues_and_prs</span>(<span class="hljs-params">repo_name, keywords</span>):
    g = Github(os.environ[<span class="hljs-string">'GITHUB_TOKEN'</span>])
    repo = g.get_repo(repo_name)

    issues = repo.get_issues(state=<span class="hljs-string">'open'</span>)
    <span class="hljs-keyword">for</span> issue <span class="hljs-keyword">in</span> issues:
        <span class="hljs-keyword">if</span> <span class="hljs-built_in">any</span>(keyword <span class="hljs-keyword">in</span> issue.title <span class="hljs-keyword">for</span> keyword <span class="hljs-keyword">in</span> keywords):
            issue.set_subscription(subscribed=<span class="hljs-literal">True</span>)

    pull_requests = repo.get_pulls(state=<span class="hljs-string">'open'</span>)
    <span class="hljs-keyword">for</span> pr <span class="hljs-keyword">in</span> pull_requests:
        <span class="hljs-keyword">if</span> <span class="hljs-built_in">any</span>(keyword <span class="hljs-keyword">in</span> pr.title <span class="hljs-keyword">for</span> keyword <span class="hljs-keyword">in</span> keywords):
            pr.set_subscription(subscribed=<span class="hljs-literal">True</span>)

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    repo_name = <span class="hljs-string">"yourusername/yourrepository"</span>  <span class="hljs-comment"># Replace with your repo</span>
    keywords = [<span class="hljs-string">"OADP"</span>, <span class="hljs-string">"backup"</span>]

    subscribe_to_issues_and_prs(repo_name, keywords)
</code></div></div></pre><p>Make sure to replace <code>"yourusername/yourrepository"</code> with the actual username and repository name.</p><p>This script subscribes to issues and PRs containing the keywords "OADP" or "backup" in their title. Make sure to have the PyGithub library installed in your environment.</p><ol start="5"><li>Commit and push your changes. The GitHub Actions workflow will now run on the specified schedule and automatically subscribe to issues and PRs containing the specified keywords in their title.</li></ol></div></div></div><div class="flex justify-between lg:block"><div class="text-gray-400 flex self-end lg:self-center justify-center mt-2 gap-2 md:gap-3 lg:gap-1 lg:absolute lg:top-0 lg:translate-x-full lg:right-0 lg:mt-0 lg:pl-2 visible"><button class="p-1 rounded-md hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-200 disabled:dark:hover:text-gray-400"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg></button><button class="p-1 rounded-md hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-200 disabled:dark:hover:text-gray-400"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"></path></svg></button></div></div></div>

## Prompt 2

Use graphql

## Response 2

<div class="relative flex w-[calc(100%-50px)] flex-col gap-1 md:gap-3 lg:w-[calc(100%-115px)]"><div class="flex flex-grow flex-col gap-3"><div class="min-h-[20px] flex flex-col items-start gap-4 whitespace-pre-wrap"><div class="markdown prose w-full break-words dark:prose-invert light"><p>To set up a GitHub Actions (GHA) workflow that runs on a schedule and subscribes to issues and pull requests containing the words "OADP" or "backup" in a repository using GraphQL, follow these steps:</p><ol><li><p>Create a new file in your repository under the <code>.github/workflows</code> directory. Name it something like <code>subscribe_to_issues_and_prs_graphql.yml</code>.</p></li><li><p>In this YAML file, define a scheduled workflow using the <code>on</code> key with a <code>schedule</code> event, and provide a cron syntax to define how often you want the workflow to run. For example, if you want it to run daily at 00:00 UTC, you would use:</p></li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>yaml</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-yaml"><span class="hljs-attr">on:</span>
  <span class="hljs-attr">schedule:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">cron:</span> <span class="hljs-string">'0 0 * * *'</span>
</code></div></div></pre><ol start="3"><li>Define the workflow steps, including setting up the environment with the necessary language and tools (e.g., Python and the <code>requests</code> library) and running a script that subscribes to the desired issues and PRs:</li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>yaml</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-yaml"><span class="hljs-attr">name:</span> <span class="hljs-string">Subscribe</span> <span class="hljs-string">to</span> <span class="hljs-string">Issues</span> <span class="hljs-string">and</span> <span class="hljs-string">PRs</span> <span class="hljs-string">using</span> <span class="hljs-string">GraphQL</span>

<span class="hljs-attr">on:</span>
  <span class="hljs-attr">schedule:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">cron:</span> <span class="hljs-string">'0 0 * * *'</span>

<span class="hljs-attr">jobs:</span>
  <span class="hljs-attr">subscribe:</span>
    <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>

    <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Set</span> <span class="hljs-string">up</span> <span class="hljs-string">Python</span>
      <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/setup-python@v2</span>
      <span class="hljs-attr">with:</span>
        <span class="hljs-attr">python-version:</span> <span class="hljs-number">3.9</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Install</span> <span class="hljs-string">dependencies</span>
      <span class="hljs-attr">run:</span> <span class="hljs-string">|
        python -m pip install --upgrade pip
        pip install requests
</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Check</span> <span class="hljs-string">issues</span> <span class="hljs-string">and</span> <span class="hljs-string">PRs</span>
      <span class="hljs-attr">env:</span>
        <span class="hljs-attr">GITHUB_TOKEN:</span> <span class="hljs-string">${{</span> <span class="hljs-string">secrets.GITHUB_TOKEN</span> <span class="hljs-string">}}</span>
      <span class="hljs-attr">run:</span> <span class="hljs-string">|
        python .github/scripts/subscribe_to_issues_and_prs_graphql.py
</span></code></div></div></pre><ol start="4"><li>In the <code>.github/scripts</code> directory of your repository, create a Python script named <code>subscribe_to_issues_and_prs_graphql.py</code>:</li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python"><span class="hljs-keyword">import</span> os
<span class="hljs-keyword">import</span> re
<span class="hljs-keyword">import</span> json
<span class="hljs-keyword">import</span> requests

<span class="hljs-keyword">def</span> <span class="hljs-title function_">run_query</span>(<span class="hljs-params">query, headers</span>):
    request = requests.post(<span class="hljs-string">"https://api.github.com/graphql"</span>, json={<span class="hljs-string">'query'</span>: query}, headers=headers)
    <span class="hljs-keyword">if</span> request.status_code == <span class="hljs-number">200</span>:
        <span class="hljs-keyword">return</span> request.json()
    <span class="hljs-keyword">else</span>:
        <span class="hljs-keyword">raise</span> Exception(<span class="hljs-string">f"Query failed with status code <span class="hljs-subst">{request.status_code}</span>. <span class="hljs-subst">{json.dumps(request.json(), indent=<span class="hljs-number">2</span>)}</span>"</span>)

<span class="hljs-keyword">def</span> <span class="hljs-title function_">subscribe_to_issues_and_prs</span>(<span class="hljs-params">owner, repo, keywords</span>):
    headers = {<span class="hljs-string">"Authorization"</span>: <span class="hljs-string">f"Bearer <span class="hljs-subst">{os.environ[<span class="hljs-string">'GITHUB_TOKEN'</span>]}</span>"</span>}
    search_query = <span class="hljs-string">f"repo:<span class="hljs-subst">{owner}</span>/<span class="hljs-subst">{repo}</span> is:open <span class="hljs-subst">{<span class="hljs-string">' '</span>.join(<span class="hljs-string">'"'</span> + keyword + <span class="hljs-string">'"'</span> <span class="hljs-keyword">for</span> keyword <span class="hljs-keyword">in</span> keywords)}</span>"</span>
    query = <span class="hljs-string">f"""
    {{
      search(query: "<span class="hljs-subst">{search_query}</span>", type: ISSUE, first: 100) {{
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
    """</span>

    result = run_query(query, headers)
    <span class="hljs-keyword">for</span> edge <span class="hljs-keyword">in</span> result[<span class="hljs-string">"data"</span>][<span class="hljs-string">"search"</span>][<span class="hljs-string">"edges"</span>]:
        node = edge[<span class="hljs-string">"node"</span>]
        node_id = node[<span class="hljs-string">"id"</span>]

        mutation = <span class="hljs-string">f"""
        mutation {{
          updateSubscription(input: {{subscribableId: "<span class="hljs-subst">{node_id}</span>", state: SUBSCRIBED}}) {{
            clientMutationId
          }}
        }}
        """</span>
        run_query(mutation, headers)

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    owner = <span class="hljs-string">"yourusername"</span>
    repo = <span class="hljs-string">"yourrepository"</span>
    keywords = [<span class="hljs-string">"OADP"</span>, <span class="hljs-string">"backup"</span>]

    subscribe_to_issues_and_prs(owner, repo, keywords)
</code></div></div></pre><p>Replace <code>"yourusername"</code> and <code>"yourrepository"</code> with your actual username and repository name.</p><p>This script subscribes to issues and PRs containing the specified keywords</p></div></div></div><div class="flex justify-between lg:block"><div class="text-gray-400 flex self-end lg:self-center justify-center mt-2 gap-2 md:gap-3 lg:gap-1 lg:absolute lg:top-0 lg:translate-x-full lg:right-0 lg:mt-0 lg:pl-2 visible"><button class="p-1 rounded-md hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-200 disabled:dark:hover:text-gray-400"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg></button><button class="p-1 rounded-md hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-200 disabled:dark:hover:text-gray-400"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"></path></svg></button></div></div></div>