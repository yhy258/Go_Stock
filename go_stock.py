from slacker import Slacker

# 내 api bot Token.
slack = Slacker('xoxb-1775081175811-1768103723574-0rr5F0Nc7mG6lNIcgzoJq3J5')

# Send a message to #general channel
# channel 이름, post.. post 부분에서 주가 부분을 넣어주면 되겠네.!

slack.chat.post_message('#stock', 'Hello fellow slackers!')

