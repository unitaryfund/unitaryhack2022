---
title: Project Maintainer Guide
metaDescription: Helpful information for project maintainers participating in unitaryhack
date: 2022-03-09
permalink: /project-guide/index.html
eleventyNavigation:
  key: Maintainers
  order: 4
---

<!-- ### Unitary Fund invites OSS project maintainers and owners to participate in unitaryhack, one of the largest quantum open source hackathons! -->

Our goal at the Unitary Fund is to build a quantum technology ecosystem that benefits the most people.
That starts by supporting and growing the great ecosystem of projects already out there that is maintained by amazing folks like _you_.

It is always important for projects to find skilled and committed contributors that can do things like help develop new functionality, maintain existing tools, and write tests and documentation. This can be challenging in open source in general, but can be _especially_ difficult for open source projects that need specialized skill sets like quantum computing. Unitaryhack shows folks what amazing projects are already out there, helping drive quantum computing forward, and helping you find new contributions for your projects.

We have some outlines below for what you can expect before and during the event, as well as [the rules for the event]({{ '/rules/' | url }}).

> **Timeline:**
>
> - March: Contact and organize participating projects and funding
> - April: Setup and test infrastructure for tagging/automation
>   - April 13th Maintainer AMA call
> - May: Review projects and finalize bounty budgets
> - June 3-17th: Hackathon starts and reviewing of PRs begins
>   - June 3rd - Hackathon Kickoff Party on Discord
>     - Review of the event + rules
>     - Answer any initial questions folks have about the event on discord
>     - Give a short intro about you project

## ⌚ Before the Hack ⌚

1. Add the `unitaryhack` to the [list of topics for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics#adding-topics-to-your-repository). as well as any issues on your projects you would like people to work on (#unitaryhack). We are looking for ~4 issues for each project (totally can be more, just a place to start) of a variety of difficulty levels.
2. Identify if there are any issues you want to put a bounty on to specifically encourage participants to tackle them. Our goal is to have at least one bounty issue per project, and we can scale that based on the size of your project’s codebase.
3. Make sure you have  `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` at the root of your repo (or similar) so folks can learn how they should make their contributions to make your life easy.
4. Make a PR to [this repo](https://github.com/unitaryfund/unitaryhack) adding your project to the [participating projects](./participating-projects.md) list with:
   1. A short description of your project with links to it,
   2. Links to the issues you would like to put bounties on, an a short description if you want of the associated issue (not necessary). We will work with you to make sure we get the bounty values correct.

    > You can see an example of a project listing by checking out the one for our project [Mitiq]([{{ '/projects/mitiq' | url }})](https://github.com/unitaryfund/unitaryhackdev/blob/main/projects/mitiq.md).

### How to choose good issues

To make sure that everyone can participate in the hackathon, we encourage project maintainers to tag a variety of issues that may or may not include quantum content, may or may not require Dev Ops skills, etc. We understand projects can be very targeted so if this is not possible that's totally fine! Our goal is to help connect eager and skilled contributors to your projects to help make the quantum open source ecosystem better 💖

If you have any questions/comments/suggestions for this event we would love to hear from you, just send us an email at [sarah@unitary.fund](mailto:sarah@unitary.fund?subject=[GitHub]%20Source%20Han%20Sans)!

## 🔨 During the Hack 🔨

As the hackathon progresses (and sometimes right away if there are eager folks who read up on the project), you should get some useful PRs!
Hackers should put `[unitaryhack]` in the title of their PRs, if they haven't please update it so they can get credit.
If a PR does not meet a minimum bar for quality, or if another PR has been accepted, please communicate on the PR conversation that it is not accepted, and tag it as `rejected` or `duplicate` as appropriate.

For bountied issues, mark the PR you want it awarded to with `unitaryhack-accepted and we will take care of sending out the bounty!

If you want a way to chat more synchronously with folks working on PRs we will be hosting workspaces on our [Discord](http://discord.unitary.fund/) channels for people to hangout and work on the hackathon together!

## Helpful resources

- [A maintainers guide to Hacktoberfest](https://medium.com/gitcoin/a-maintainers-guide-to-hacktoberfest-21405c8ff09f)
- [Tips and tricks for maintaining your repo and your mental health](https://www.twilio.com/blog/how-to-hacktoberfest-tips-and-tricks-for-maintaining-your-repo-and-your-mental-health)
- [Promoting your open source project](https://github.com/zenika-open-source/promote-open-source-project/blob/master/README.md)
- [Write the docs guide](https://www.writethedocs.org/guide/)
