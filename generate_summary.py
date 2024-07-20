import os
from datetime import datetime, timedelta
from github import Github

# Authenticate to GitHub
g = Github(os.getenv('GITHUB_TOKEN'))

# Get the repository
repo = g.get_repo("your-username/your-repo")

# Get commits from the last day
since = datetime.now() - timedelta(days=1)
commits = repo.get_commits(since=since)

# Generate summary
summary = "# Daily Commit Summary\n\n"
summary += f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n"
for commit in commits:
    summary += f"- {commit.commit.message} by {commit.commit.author.name}\n"

# Write summary to file with date in filename
filename = f"summary_{datetime.now().strftime('%Y-%m-%d')}.md"
with open(filename, "w") as f:
    f.write(summary)
