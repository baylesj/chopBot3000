#!/bin/bash
curl -X POST \
     -F 'token=gIkuvaNzQIHg97ATvDxqgjtO' \
     -F 'team_id=T0001' \
     -F 'team_domain=example' \
     -F 'channel_id=C21471' \
     -F 'channel_name=test' \
     -F 'user_id=U2147483697' \
     -F 'user_name=Stevie' \
     -F 'command=/weather' \
     -F "text=$1" \
     -F 'response_url=https://hooks.slack.com/commands/1234/5678' \
    localhost:5000
