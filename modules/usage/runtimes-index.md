---
title: "Runtime Configuration"
description: "<Note>
```
This section is for users that would like to use a runtime other than Docker for OpenHands. 
</Note>"
---
```
</CodeGroup>

<Note>
```
This section is for users that would like to use a runtime other than Docker for OpenHands.
```
</CodeGroup>

</Note>
```
A Runtime is an environment where the OpenHands agent can edit files and run
commands.
```
</CodeGroup>

By default, OpenHands uses a [Docker-based runtime](/modules/usage/docker), running on your local computer.
This means you only have to pay for the LLM you're using, and your code is only ever sent to the LLM.

We also support other runtimes, which are typically managed by third-parties.

Additionally, we provide a [Local Runtime](/modules/usage/local) that runs directly on your machine without Docker,
which can be useful in controlled environments like CI pipelines.

## Available Runtimes

OpenHands supports several different runtime environments:

- [Docker Runtime](/modules/usage//modules/usage/docker) - The default runtime that uses Docker containers for isolation (recommended for most users).
- [OpenHands Remote Runtime](/modules/usage//modules/usage/remote) - Cloud-based runtime for parallel execution (beta).
- [Modal Runtime](/modules/usage//modules/usage/modal) - Runtime provided by our partners at Modal.
- [Daytona Runtime](/modules/usage//modules/usage/daytona) - Runtime provided by Daytona.
- [Local Runtime](/modules/usage//modules/usage/local) - Direct execution on your local machine without Docker.
