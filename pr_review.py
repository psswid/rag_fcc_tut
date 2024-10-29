import os
from dotenv import load_dotenv
from pr_agent import cli
from pr_agent.config_loader import get_settings

def main():
    load_dotenv()
    # Fill in the following values
    provider = "github" # github/gitlab/bitbucket/azure_devops
    user_token = os.getenv("USER_TOKEN")  #  user token for github repo
    openai_key = os.getenv("AZURE_API_KEY")  # OpenAI key
    pr_url = "https://github.com/psswid/rag_fcc_tut/pull/4"      # PR URL, for example 'https://github.com/Codium-ai/pr-agent/pull/809'
    command = "/review" # Command to run (e.g. '/review', '/describe', '/ask="What is the purpose of this PR?"', ...)

    # Setting the configurations
    get_settings().set("CONFIG.git_provider", provider)
    get_settings().set("openai.key", openai_key)
    get_settings().set("github.user_token", user_token)

    # Run the command. Feedback will appear in GitHub PR comments
    cli.run_command(pr_url, command)


if __name__ == '__main__':
    main()