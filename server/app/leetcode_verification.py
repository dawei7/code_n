import urllib.request
import json
import logging
from typing import Optional

logger = logging.getLogger(__name__)

def check_leetcode_solved(username: str, problem_slug: str) -> tuple[bool, str]:
    """Check if username has an Accepted submission for problem_slug on LeetCode.
    
    Returns (success, message).
    """
    url = "https://leetcode.com/graphql"
    query = """
    query recentSubmissions($username: String!, $limit: Int) {
        recentSubmissionList(username: $username, limit: $limit) {
            titleSlug
            statusDisplay
        }
    }
    """
    payload = {
        "query": query,
        "variables": {
            "username": username,
            "limit": 20
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://leetcode.com"
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = response.read().decode("utf-8")
            data = json.loads(res_data)
            
            # Check for GraphQL errors
            if "errors" in data and data["errors"]:
                return False, data["errors"][0].get("message", "LeetCode GraphQL error")
                
            submissions = data.get("data", {}).get("recentSubmissionList", [])
            if not submissions:
                return False, f"No recent submissions found for LeetCode user '{username}'. Please ensure the username is correct and your profile is public."
                
            for sub in submissions:
                # normalize strings
                sub_slug = str(sub.get("titleSlug", "")).lower().strip()
                target_slug = problem_slug.lower().strip()
                status = str(sub.get("statusDisplay", ""))
                
                if sub_slug == target_slug and status == "Accepted":
                    return True, "Accepted submission found!"
                    
            return False, f"Could not find an 'Accepted' submission for slug '{problem_slug}' in the last 20 submissions on LeetCode."
    except Exception as e:
        logger.error(f"LeetCode verification failed: {e}")
        return False, f"Network error connecting to LeetCode: {str(e)}. Please check your internet connection or try again later."
