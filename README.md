# ssh-agent-sign
Simple Python script to have an active `ssh-agent` sign a message.

## Usage:

Just pipe:

    echo "Hello" | python -m ssh-agent-sign > hello.sig
