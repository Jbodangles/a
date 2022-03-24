from instapy import InstaPy

session = InstaPy(username="jordans_fit", password="Riverstone,13", headless_browser=True)
session.login()
session.set_quota_supervisor(enabled=True, peak_comments_daily=250, peak_comments_hourly=25)
session.set_relationship_bounds(enabled=True, max_followers= 5000)
session.like_by_tags(["fitness", "workout", "Alphalete"], 20)
session.set_dont_like(["naked", "fail"])
session.set_do_follow(True, percentage = 25)
session.set_do_comment (True, percentage = 75)
session.set_comments(["Very Nice, Keep it Up!", "Nice Progress", "#Gains"])
session.end()