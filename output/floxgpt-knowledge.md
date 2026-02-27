# Flox Documentation - Complete Knowledge Base

> **Purpose**: This document contains the complete Flox documentation, consolidated for use by FloxGPT, a custom GPT assistant.

## Metadata

- **Last Updated**: 2026-02-27 06:59:27 UTC
- **Source Repository**: https://github.com/flox/floxdocs
- **Source Commit**: `6cffa11a`
- **Source Commit Date**: 2026-02-25 17:00:34 -0700
- **Source Commit Message**: fix: Move scarf integration into mkdocs.yml file

## About Flox

Flox is a virtual environment and package manager all in one. With Flox you can:

- Create reproducible development environments that work across Linux and macOS
- Install packages from the largest open-source package repository (Nixpkgs)
- Share environments with your team using FloxHub or Git
- Run services and background processes within your environment
- Build and publish your own packages

Flox provides a friendly CLI that abstracts away the complexity of Nix while giving you access to its powerful features.

## Table of Contents

- [What is Flox?](#what-is-flox)
- [Install Flox { #install-flox }](#install-flox--install-flox-)
- [Replacing A Nix Installation](#replacing-a-nix-installation)
- [Uninstall Flox { #uninstall-flox }](#uninstall-flox--uninstall-flox-)
- [Uninstall](#uninstall)
- [Creating environments](#creating-environments)
- [Customizing the shell environment](#customizing-the-shell-environment)
- [What is a Flox environment?](#what-is-a-flox-environment)
- [Floxhub Environments](#floxhub-environments)
- [Layering multiple environments](#layering-multiple-environments)
- [Designing cross-platform environments](#designing-cross-platform-environments)
- [Sharing your environments](#sharing-your-environments)
- [What is the Flox Catalog?](#what-is-the-flox-catalog)
- [Manifest Builds](#manifest-builds)
- [Services](#services)
- [Troubleshooting](#troubleshooting)
- [Activating environments](#activating-environments)
- [What is the Base Catalog](#what-is-the-base-catalog)
- [Building with Flox](#building-with-flox)
- [Builds](#builds)
- [C/C++](#cc)
- [Setting up a Catalog Store](#setting-up-a-catalog-store)
- [Continuous integration/delivery (CI/CD)](#continuous-integrationdelivery-cicd)
- [Composing environments](#composing-environments)
- [Reusing and combining developer environments](#reusing-and-combining-developer-environments)
- [Configuration](#configuration)
- [Flox + CUDA tutorial](#flox--cuda-tutorial)
- [The default environment](#the-default-environment)
- [adjust this to match your existing or desired node group configuration -- below values are examples](#adjust-this-to-match-your-existing-or-desired-node-group-configuration----below-values-are-examples)
- [Flox in 5 minutes](#flox-in-5-minutes)
- [Flox vs. container workflows](#flox-vs-container-workflows)
- [What is FloxHub?](#what-is-floxhub)
- [What is a generation?](#what-is-a-generation)
- [Gitlab Ci](#gitlab-ci)
- [Go](#go)
- [Homebrew migration guide](#homebrew-migration-guide)
- [Intro](#intro)
- [JVM](#jvm)
- [K8S Shim Cli Version](#k8s-shim-cli-version)
- [Kind Demo](#kind-demo)
- [Known issues](#known-issues)
- [Nix Expression Builds](#nix-expression-builds)
- [Node.js](#nodejs)
- [Node Version Manager (nvm) migration guide](#node-version-manager-nvm-migration-guide)
- [Understanding Organizations in FloxHub](#understanding-organizations-in-floxhub)
- [Paid Feature](#paid-feature)
- [manifest.toml](#manifesttoml)
- [Python](#python)
- [Ruby](#ruby)
- [Rust](#rust)
- [Self Managed](#self-managed)
- [Signing keys](#signing-keys)
- [The Tech Behind Imageless Kubernetes](#the-tech-behind-imageless-kubernetes)
- [Upgrading](#upgrading)

---

# Documentation Content


## What is Flox?

> Source: `index.md`

---
title: Introduction
description: What is Flox?

---


# What is Flox?

Flox is a next-generation, language-agnostic package and environment manager.

- Define everything your environment needs—packages, tools, environment variables, and services—in one manifest.
- Switch between environments easily, share them with your team, and keep everything in version control.
- Use the same setup across macOS and Linux, on both x86 and Arm.

Flox achieves isolation through pre-configured sub-shells, not containers, so it works seamlessly with your existing tools, shells, and dotfiles. Under the hood, Flox uses Nix to ensure reproducibility—without requiring you to learn Nix.

Flox makes it easy to work locally, test in CI, and deploy to production—all with the same environment.


 <iframe width="550" height="300" src="https://www.youtube.com/embed/aidi5svDml8?si=rrgQ6a0oQzdFNgWs" title="What is Flox?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Get Started
<div class="grid cards" markdown>

-   :octicons-terminal-24:{ .lg .middle } __Quick start with the Flox CLI__

    ---

    Install `flox` with `apt`, `yum`, `brew`, or a standalone installer to get your dev
    environment set up in minutes.

    [:octicons-arrow-right-24: Download & Install][install_flox]

    [:octicons-arrow-right-24: Flox in 5 minutes][flox_5_minutes]

    [:octicons-arrow-right-24: Search packages in FloxHub][floxhub_packages]{:target="_blank"}

-   :material-nix:{ .lg .middle } __Already using Nix? Start here__

    ---

    Flox brings the power of Nix to your team, and can simplify your workflows.

    [:octicons-arrow-right-24: Install Flox with flakes or profiles](install-flox/install.md#__tabbed_1_5){:target="_blank"}

    [:octicons-arrow-right-24: Flox brings Nix to your teams](https://flox.dev/blog/enterprise-nix-its-time-to-bring-nix-to-work/){:target="_blank"}

    [:octicons-arrow-right-24: Use flakes in Flox](https://flox.dev/blog/extending-flox-with-nix-flakes/){:target="_blank"}

</div>

Examples for getting started in just a few of the many languages Flox supports:

[Node :simple-nodedotjs:](https://flox.dev/blog/using-flox-to-create-portable-reproducible-nodejs-environments/){ .md-button }
[Go :fontawesome-brands-golang:](https://flox.dev/blog/using-flox-to-create-portable-reproducible-go-environments/){ .md-button }
[Python :fontawesome-brands-python:](https://flox.dev/blog/using-flox-to-create-portable-reproducible-python-environments/){ .md-button }
[Rust :fontawesome-brands-rust:](https://flox.dev/blog/a-real-world-rust-project-with-flox/){ .md-button }
[Ruby :material-language-ruby:](https://flox.dev/blog/making-ruby-projects-easier-to-share/){ .md-button }

---

## Why Flox?

We encounter the same challenges, no matter the stack: inconsistent environments, dependency drift, and brittle build processes that don’t scale well across machines, teams, or deployment targets. Current solutions often add complexity and fragmentation.

Flox takes a different approach: it provides a consistent, language-agnostic workflow for managing environments, from local development to CI to production.

Use Flox to solve three common use cases:

- Reproducible dev environments
- Reliable package management across systems
- Consistent builds from local to production

### __Reproducible dev environments__

Set up a [local developer environment](https://flox.dev/docs/tutorials/creating-environments/) that will work the same across multiple operating systems and architectures. Seamlessly switch between development environments across multiple language ecosystems using a consistent, unified workflow.

Declare all the packages, activation scripts, environment variables and [services](https://flox.dev/docs/concepts/services/) needed to reproduce the environment in a simple manifest that can be checked into [version control along with your source code](https://flox.dev/blog/flox-and-teams-managing-your-code-and-your-runtime-environment-in-just-one-place/).

Once your environment is configured, you can simplify the setup instructions in your README to a single command (`flox activate`), making it easy to [share environments](https://flox.dev/blog/flox-and-teams-using-shared-flox-environments/) and [onboard new developers](https://flox.dev/blog/flox-and-teams-onboarding-made-easy-with-github-and-flox/).


### __Cross-platform package management for your whole system__

Set up your [default environment](https://flox.dev/docs/tutorials/default-environment/) with a set of
packages that you always want available, whether you're on macOS or Linux—x86 or Arm.

Then, when you need to [set up a new laptop](https://flox.dev/blog/setting-up-a-new-laptop-made-easy-with-flox/
), or [keep multiple machines in sync](https://flox.dev/docs/tutorials/sharing-environments/#always-using-the-same-environment-across-multiple-devices
), you can be sure you're using the exact same versions, no matter when or where you need them.

If you're already using Homebrew, you can easily [migrate or use Homebrew and Flox together](https://flox.dev/docs/tutorials/migrations/homebrew/).


### __Consistent builds from local to CI to production__

Flox lets you define what an environment _is_ in a way that can be reused across local dev, CI, and production.
Leverage [pre-built integrations](https://flox.dev/docs/tutorials/ci-cd/?h=ci) for GitHub Actions, CircleCI, and GitLab to pull and activate the same environments locally, in CI and in production.

Or use Flox [containerize](https://flox.dev/docs/man/flox-containerize/?h=containerize) to package your environments as OCI images—fully pinned and runnable anywhere.
From bare metal to VMs, from Docker Swarm to Kubernetes to AWS Lambda—the runtime context might change, but Flox environments run and behave the same everywhere.

Need an example? See how [the Flox Docs team uses Flox in CI](https://flox.dev/blog/integrating-flox-with-ci-for-consistent-reproducible-dev-environments/) to build, test and deploy this docs site.


### __And more...__

- Create templates or reusable toolchains to bootstrap new projects by [reusing and combining dev environments](https://flox.dev/docs/tutorials/composition/).

- Create a portable [environment with transparent auth](https://flox.dev/blog/get-your-preferred-secrets-manager-in-a-portable-cross-platform-cli-toolkit/) via a third-party secrets manager so cross-platform workflows work the same everywhere: locally, in CI, or in production.

## __Have questions?__

__Ask us on [Slack :fontawesome-brands-slack:](https://go.flox.dev/slack){:target="_blank"} or [Discourse :fontawesome-brands-discourse:](https://discourse.flox.dev){:target="_blank"}__

The Flox product and engineering teams love to hear directly from users. Your questions and feedback will help us prioritize the improvements to the product that matter most to you.


[install_flox]: ./install-flox/install.md
[flox_5_minutes]: ./flox-5-minutes.md
[create_guide]: ./tutorials/creating-environments.md
[share_guide]: ./tutorials/sharing-environments.md
[init]: ./man/flox-init.md
[search]: ./man/flox-search.md
[show]: ./man/flox-show.md
[catalog]: ./concepts/packages-and-catalog.md
[install]: ./man/flox-install.md
[activate]: ./man/flox-activate.md
[edit]: ./man/flox-edit.md
[push]: ./man/flox-push.md
[pull]: ./man/flox-pull.md
[delete]: ./man/flox-delete.md
[list]: ./man/flox-list.md
[manifest]: ./man/manifest.toml.md
[rust-cookbook]: ./languages/rust.md
[multi-arch]: ./tutorials/multi-arch-environments.md
[config]: ./man/flox-config.md
[services]: ./concepts/services.md
[floxhub_packages]: https://hub.flox.dev/packages

---


## Install Flox { #install-flox }

> Source: `install-flox/install.md`

---
title: Install Flox
description: How to install or upgrade the Flox CLI
---

# Install Flox { #install-flox }

=== "MacOS - Pkg"

    **Download and install the package that matches your machine's architecture.**

    1. Download installer for Macs with

        [Apple Silicon][flox_mac_apple_silicon_install]{:target="_blank" .md-button .md-button--primary}
        [Intel processors][flox_mac_intel_install]{:target="_blank" .md-button .md-button--primary}

    2. Double-click to install the downloaded file
    3. Open a terminal window to continue below

            {%
            include-markdown "include/replacing-a-Nix-installation.md"
        %}

    **Verify Flox installation**

    If the following command returns without error then you're ready to get
    started!

    ```console
    $ flox --version # (1)!
    {{ FLOX_VERSION }}

    ```

    4.  The version you will see might be different.

    **Upgrades to existing Flox installation**

    Download and install the latest image as described above.

=== "MacOS - Homebrew"

    **Brew install**

    In your terminal run:

    ``` { .sh .code-command .copy }
    brew install flox
    ```

            You may be prompted for a `sudo` password or be asked if your terminal has authorization to modify disk contents.


            {%
            include-markdown "include/replacing-a-Nix-installation.md"
        %}


    **Verify Flox installation**

    If the following command returns without error then you're ready to get
    started!

    ```console
    $ flox --version # (1)!
    {{ FLOX_VERSION }}

    ```

    1.  The version you will see might be different.

    **Upgrade existing Flox installation**

    ``` { .sh .code-command .copy }
    brew upgrade flox
    ```

=== "Debian"

    For use on Debian, Ubuntu, and other Debian-based distributions.

            The package will register a new source in `/etc/apt/sources.list.d` to enable upgrades via `apt`.

    **Download and install the package**

    1. Download flox.deb for your system architecture:

         [64-bit Intel/AMD][flox_x86_64_deb_install]{:target="_blank" .md-button .md-button--primary}
         [64-bit ARM][flox_aarch64_deb_install]{:target="_blank" .md-button .md-button--primary}

    1. Install the downloaded file

        ```{ .sh .code-command .copy }
        sudo apt install /path/to/flox.deb
        ```

            {%
            include-markdown "include/replacing-a-Nix-installation.md"
        %}

    **Verify Flox installation**

    If the following command returns without error then you're ready to get
    started!

    ``` console
    $ flox --version # (1)!
    {{ FLOX_VERSION }}

    ```

    1.  The version you will see might be different.

    **Upgrade existing Flox installation**

    ``` { .sh .code-command .copy }
    sudo apt update;
    sudo apt --only-upgrade install flox
    ```

=== "RPM"

    For use on RedHat, CentOS, Amazon Linux, and other RPM-based distributions.

            The rpm will register a package repository in `/etc/yum.repos.d` to enable upgrades.
        via `yum`, `dnf` and other compatible tools.

    **Download and install the package**

    1. Download flox.rpm for your system architecture:

         [64-bit Intel/AMD][flox_x86_64_rpm_install]{:target="_blank" .md-button .md-button--primary}
         [64-bit ARM][flox_aarch64_rpm_install]{:target="_blank" .md-button .md-button--primary}

    1. Install the downloaded file

        ```{ .sh .code-command .copy }
        sudo rpm --import https://downloads.flox.dev/by-env/stable/rpm/flox-archive-keyring.asc
        sudo rpm -ivh /path/to/flox.rpm
        ```

            {%
            include-markdown "include/replacing-a-Nix-installation.md"
        %}

    **Verify Flox installation**

    If the following command returns without error then you're ready to get
    started!

    ```console
    $ flox --version # (1)!
    {{ FLOX_VERSION }}

    ```

    1.  The version you will see might be different.

    **Upgrade existing Flox installation**

    ``` { .sh .code-command .copy }
    sudo yum update flox
    ```

    or

    ``` { .sh .code-command .copy }
    sudo dnf update flox
    ```

=== "Nix - Generic"


        Use the Flox installer for your system to allow some opinionated configuration of Nix, or use these "Nix - Generic" instructions for full control of your Nix installation.

    **Install Nix**

    Please ensure you are using Nix version `2.18.0` or greater.

    **Install Flox with Nix imperatively**

    * Configure Substituters

        Add the following values to `/etc/nix/nix.conf`, taking care to merge them
        with any `trusted-substituters` or `trusted-public-keys` values that may
        already be defined:

        ``` title="/etc/nix/nix.conf"
        extra-trusted-substituters = https://cache.flox.dev
        extra-trusted-public-keys = {{ FLOX_PUBLIC_KEY }}
        ```

        Then restart the `nix-daemon`, if applicable:

        * Linux:
            ```{ .sh .code-command .copy-2 }
            sudo systemctl stop nix-daemon.service
            sudo systemctl restart nix-daemon.socket
            ```
        * MacOS:
            ```{ .sh .code-command .copy-2 }
            sudo launchctl kickstart -k -p system/org.nixos.nix-daemon
            ```

    * Install Flox to your _personal_ profile:

        ```{ .sh .code-command .copy }
        nix profile install \
              --experimental-features "nix-command flakes" \
              --accept-flake-config \
              'github:flox/flox/latest'
        ```

    * Install Flox to the system-wide `default` profile as root:

        ```{ .sh .code-command .copy }
        sudo -H nix profile install \
              --profile /nix/var/nix/profiles/default \
              --experimental-features "nix-command flakes" \
              --accept-flake-config \
              'github:flox/flox/latest'
        ```

        If you encounter the following error then please upgrade your Nix
        installation (and in particular the running `nix-daemon`) to the latest
        version (minimum supported version is `2.18.0`):

        ```text
        error: builder for '/nix/store/35l1qqyis11y88ic0cp3yxgv3286l4pb-flox-0.0.2-r295.drv' failed with exit code 1;
               last 1 log lines:
               > error: attribute 'requisites' missing
        ```

        If you encounter any other errors with the installer please report the
        bug by way of [discourse][flox_discourse]{:target="_blank"}, including
        a full copy of the command invoked and error encountered.


    **Install Flox with Nix declaratively**

    The following example is for a Nix darwin installation.
    You may need to modify inputs to match your system.


        Flox hosts a binary cache for its packages, that can be added to your `/etc/nix/nix.conf` file.
        We recommend doing this if you are installing Flox system-wide.

        ``` title="/etc/nix/nix.conf"
        extra-trusted-substituters = https://cache.flox.dev
        extra-trusted-public-keys = {{ FLOX_PUBLIC_KEY }}
        ```

        Or, to your flake configuration by using the `nixConfig` attribute.
        This will ensure that Flox's binary cache is used for all operation within that flake.

        ```title="flake.nix"
        {
            nixConfig = {
                extra-trusted-substituters = ["https://cache.flox.dev"];
                extra-trusted-public-keys = ["flox-cache-public-1:7F4OyH7ZCnFhcze3fJdfyXYLQw/aV7GEed86nQ7IsOs="];
            };
        }
        ```

        Note that if you don't add either of these options, Flox will be built from source, together with a patched version of Nix.
        Which might take a while on less powerful systems.

    ```{ .sh .code-command .copy}
    {
      decription = "Example Darwin system flake";

      nixConfig = {
        extra-trusted-substituters = ["https://cache.flox.dev"];
        extra-trusted-public-keys = ["flox-cache-public-1:7F4OyH7ZCnFhcze3fJdfyXYLQw/aV7GEed86nQ7IsOs="];
      };

      inputs = {
        nixpkgs = {
          url = "github:NixOS/nixpkgs/nixpkgs-23.11-darwin";
        };
        nix-darwin = {
          url = "github:LnL7/nix-darwin";
          inputs.nixpkgs.follows = "nixpkgs";
        };
        flox = {
          url = "github:flox/flox/latest";
        };
      };

      outputs = inputs@{ self, nix-darwin, nixpkgs, flox }:
      let
        configuration = { pkgs, ... }: {
          environment.systemPackages =
            [ pkgs.{{ YOUR_PACKAGES }}
              inputs.flox.packages.${pkgs.system}.default
            ];

          nix.settings = {
            experimental-features = "nix-command flakes";
            substituters = [
              "https://cache.flox.dev"
            ];
            trusted-public-keys = [
              "flox-cache-public-1:7F4OyH7ZCnFhcze3fJdfyXYLQw/aV7GEed86nQ7IsOs="
            ];
          };

          {{ YOUR_CONFIG }}
        };
      in
      {
        darwinConfigurations."{{ YOUR_HOST }}" = nix-darwin.lib.darwinSystem {
          modules = [ configuration ];
          specialArgs = { inherit inputs; };
        };
      };
    }

    ```

    Run `nix-darwin` to install the configuration and packages you’ve declared.
    This is an example on `nix-darwin`: `nix run nix-darwin -- switch --flake ~/path/to/flake`

    **Verify Flox installation**

    If the following command returns without error then you're ready to get
    started!

    ```console
    $ flox --version # (1)!
    {{ FLOX_VERSION }}

    ```

    1.  The version you will see might be different.


    **Upgrade existing Flox installation**

    If you've installed Flox to the system-wide `default` profile

    ``` { .sh .code-command .copy }
    sudo -H nix profile upgrade \
            --profile /nix/var/nix/profiles/default \
            --experimental-features "nix-command flakes" \
            --accept-flake-config \
            '.*flox'
    ```

    Or, if you've installed Flox to your own _personal_ profile

    ``` { .sh .code-command .copy }
    nix profile upgrade \
        --experimental-features "nix-command flakes" \
        --accept-flake-config \
        '.*flox'
    ```

    Or, if you've declared Flox using a flake, run `nix flake update`.

=== "Nix - NixOS"

    **Configure Substituters**

    Similarly configure `/etc/nixos/configuration.nix` to add the lines:

    ``` text title="/etc/nixos/configuration.nix"
    nix.settings.trusted-substituters = [ "https://cache.flox.dev" ];
    nix.settings.trusted-public-keys = [ "{{ FLOX_PUBLIC_KEY }}" ];
    ```

    ... and then invoke:

    ```{ .sh .code-command .copy }
    sudo nixos-rebuild switch
    ```

    **Install Flox**

    * Install to your _personal_ profile:

        ```{ .sh .code-command .copy }
        nix profile install \
              --experimental-features "nix-command flakes" \
              --accept-flake-config \
              'github:flox/flox/latest'
        ```

    * Install Flox to the system-wide `default` profile as root:

        ```{ .sh .code-command .copy }
        sudo -H nix profile install \
              --profile /nix/var/nix/profiles/default \
              --experimental-features "nix-command flakes" \
              --accept-flake-config \
              'github:flox/flox/latest'
        ```


        If you encounter the following error then please upgrade your Nix
        installation (and in particular the running `nix-daemon`) to the latest
        version (minimum supported version is `2.18.0`):

        ```text
        error: builder for '/nix/store/35l1qqyis11y88ic0cp3yxgv3286l4pb-flox-0.0.2-r295.drv' failed with exit code 1;
               last 1 log lines:
               > error: attribute 'requisites' missing
        ```

        If you encounter any other errors with the installer please report the
        bug by way of [discourse][flox_discourse]{:target="_blank"}, including
        a full copy of the command invoked and error encountered.

    **Verify Flox installation**

    If the following command returns without error then you're ready to get
    started!

    ```console
    $ flox --version # (1)!
    {{ FLOX_VERSION }}

    ```

    1.  The version you will see might be different.

=== "Container"

    If you have Docker installed then you can also run flox in a container to
    try it out before installing on your system.

    **Invoke Flox container**

    ``` { .sh .code-command .copy }
    docker run --pull always --rm -it ghcr.io/flox/flox
    ```

    **Verify Flox installation**

    If the following command returns without error then you're ready to get
    started!

    ``` console
    $ flox --version # (1)!
    {{ FLOX_VERSION }}

    ```

    1.  The version you will see might be different.

=== "WSL 2"



        Please install and configure **WSL version 2** as described in the
        Microsoft Learn [Install
        WSL](https://learn.microsoft.com/en-us/windows/wsl/install){:target="_blank"}
        guide before installing Flox. Please also [ensure the
        state](https://learn.microsoft.com/en-us/windows/wsl/basic-commands)
        (whether the distribution is running or stopped) is running.

        Note that installation will fail on WSL 1.

    Microsoft provides several Linux distributions for use with WSL and will
    use Ubuntu by default. Use the following commands to run and manage your
    chosen distribution:

    * list installed distributions: `wsl --list`
    * run specified distribution: `wsl --distribution <name>`
    * list all available distributions: `wsl --list --online`
    * install distribution: `wsl --install -d <name>`
    * terminate distribution: `wsl --terminate <name>`
    * unregister and delete distribution: `wsl --unregister <name>`

    **Supported distributions**

    Please follow the steps below to install Flox on the distribution of your
    choice:


        **Download and install the package**

        1. Download flox.deb for your system architecture:

             [64-bit Intel/AMD][flox_x86_64_deb_install]{:target="_blank" .md-button .md-button--primary}
             [64-bit ARM][flox_aarch64_deb_install]{:target="_blank" .md-button .md-button--primary}

        1. Install the downloaded file

            ```{ .sh .code-command .copy }
            sudo dpkg -i /path/to/flox.deb
            ```


        **Install prerequisites**

        ```{ .sh .code-command .copy }
        sudo apt-get install policycoreutils semodule-utils tar wget xz-utils
        ```

        **Download and install the package**

        1. Download flox.deb for your system architecture:

             [64-bit Intel/AMD][flox_x86_64_deb_install]{:target="_blank" .md-button .md-button--primary}
             [64-bit ARM][flox_aarch64_deb_install]{:target="_blank" .md-button .md-button--primary}

        1. Install the downloaded file

            ```{ .sh .code-command .copy }
            sudo dpkg -i /path/to/flox.deb
            ```


        **Install prerequisites**

        ```{ .sh .code-command .copy }
        sudo yum install tar xz
        ```

        **Download and install the package**

        1. Download flox.rpm for your system architecture:

             [64-bit Intel/AMD][flox_x86_64_rpm_install]{:target="_blank" .md-button .md-button--primary}
             [64-bit ARM][flox_aarch64_rpm_install]{:target="_blank" .md-button .md-button--primary}

        1. Install the downloaded file


            ```{ .sh .code-command .copy }
            sudo rpm -ivh /path/to/flox.rpm
            ```


        You will encounter the following warning during the installation:

        ```text
        ---- warning! ------------------------------------------------------------------
        We did not detect systemd on your system. With a multi-user install
        without systemd you will have to manually configure your init system to
        launch the Nix daemon after installation.
        ```

        You can disregard this message as we will be configuring the
        `nix-daemon` to start automatically in the next section.

    **Configure `nix-daemon` to start on activation**

    Once Flox has been installed on your WSL distribution the `nix-daemon` will
    need to be automatically started as you start your WSL instance.

    Run the following command to add the necessary logic to invoke `nix-daemon`
    by way of your `~/.bashrc` file:

    ```{ .sh .code-command .copy }
    cat >> ~/.bashrc <<EOF
    ( wsl.exe -d $WSL_DISTRO_NAME -u root service nix-daemon status 2>&1 >/dev/null ) || wsl.exe -d $WSL_DISTRO_NAME -u root service nix-daemon start
    EOF
    ```

    Then restart your WSL shell (or start another) and run the following
    command to ensure that the `nix-daemon` is working correctly:

    ```{ .sh .code-command .copy }
    nix --extra-experimental-features nix-command store ping
    ```
    **Verify Flox installation**

    If the following command returns without error then you're ready to get
    started!

    ```console
    $ flox --version # (1)!
    {{ FLOX_VERSION }}

    ```

    1.  The version you will see might be different.

    **Upgrade existing Flox installation**

    Please follow the instructions provided on either the Debian or RPM tab
    (whichever matches the existing Linux Distribution installed with your
    WSL) to update to latest version of Flox.

[flox]: https://flox.dev
[flox_x86_64_deb_install]: https://downloads.flox.dev/by-env/stable/deb/flox-{{ FLOX_VERSION }}.x86_64-linux.deb
[flox_aarch64_deb_install]: https://downloads.flox.dev/by-env/stable/deb/flox-{{ FLOX_VERSION }}.aarch64-linux.deb
[flox_x86_64_rpm_install]: https://downloads.flox.dev/by-env/stable/rpm/flox-{{ FLOX_VERSION }}.x86_64-linux.rpm
[flox_aarch64_rpm_install]: https://downloads.flox.dev/by-env/stable/rpm/flox-{{ FLOX_VERSION }}.aarch64-linux.rpm
[flox_mac_apple_silicon_install]: https://downloads.flox.dev/by-env/stable/osx/flox-{{ FLOX_VERSION }}.aarch64-darwin.pkg
[flox_mac_intel_install]: https://downloads.flox.dev/by-env/stable/osx/flox-{{ FLOX_VERSION }}.x86_64-darwin.pkg
[flox_discourse]: https://discourse.flox.dev
[release_notes]: https://github.com/flox/flox/releases

---


## Replacing A Nix Installation

> Source: `include/replacing-a-Nix-installation.md`

The Flox installer will perform some opinionated configuration of Nix, but Nix will still be usable.
If you want full control of your Nix installation, see the instructions for installing Flox in the "Nix - Generic" tab above.

When installing over a previous installation of Nix the Flox installation
will:

1. Back out customizations made to the following files when Nix was
    installed:
    * `/etc/bashrc`
    * `/etc/bash.bashrc`
    * `/etc/profile.d/nix.sh`
    * `/etc/zshrc`
    * `/etc/zsh/zshrc`
1. Overwrite the system-wide `/etc/nix/nix.conf`
1. (If applicable) convert the Nix installation to a multi-user install
1. Reconfigure the `nix-daemon` invocation

These changes are designed to improve the overall user experience and make the Nix installation more reliable and easier to support, but it's worth noting that **anyone wishing to revert to a "vanilla" Nix installation after installing Flox will need to re-install Nix**.

If you are installing over a previous installation of Nix we suggest that you install Flox to a test machine or VM to gain familiarity with it first.

The version of Nix installed by Flox tracks the stable version of Nix in nixpkgs, occasionally adding additional backports or patches.
Nix is usually updated monthly, although if Nix makes breaking changes, updates may be less frequent.

---


## Uninstall Flox { #uninstall-flox }

> Source: `install-flox/uninstall.md`

---
title: Uninstall Flox
description: How to uninstall the Flox CLI
---

# Uninstall Flox { #uninstall-flox }

While we are sad we see you uninstalling `flox` we would like **thank you**
for giving `flox` a try.

As we try to improve `flox` we really appreciate any feedback, especially
where we failed. We like to know what was not working or where could we do
a better job. Please reach us [via
discourse][flox_discourse]{:target="_blank"} or [via
email](mailto:hello@flox.dev).

Here's how to **completely remove `flox` from your system**.

=== "MacOS - Pkg"


    Be sure to back up the system and/or extract any important Nix-related
    files and packages before continuing.

    1. Ensure no running processes are using `/nix`.

    1. Run:

        ``` { .text .code-command .copy }
        sudo /usr/local/share/flox/scripts/uninstall
        ```

    Regardless of the current state, brew can be used to perform a full clean up:
    ``` { .text .code-command .copy }
    brew uninstall --force --zap flox
    ```

    We recommend rebooting your system after uninstalling Flox.
=== "MacOS - Homebrew"


    Be sure to back up the system and/or extract any important Nix-related
    files and packages before continuing.


    Run:

    ``` { .text .code-command .copy }
    brew uninstall flox
    ```

    To remove all traces of flox including user preferences uninstall with:

    ``` { .text .code-command .copy }
    brew uninstall --zap flox
    ```

    In the case of recovering a partial install, a force and zap can help:
    ``` { .text .code-command .copy }
    brew uninstall --force --zap flox
    ```

    We recommend rebooting your system after uninstalling Flox.

=== "Debian"

    For use on Debian, Ubuntu, and other Debian-based distributions.


    Be sure to back up the system and/or extract any important Nix-related
    files and packages before continuing.

    ``` { .text .code-command .copy }
    sudo apt-get purge flox
    ```

    We recommend rebooting your system after uninstalling Flox.

=== "RPM"

    For use on RedHat, CentOS, Amazon Linux, and other RPM-based
    distributions.


    Be sure to back up the system and/or extract any important Nix-related
    files and packages before continuing.

    ``` { .text .code-command .copy }
    sudo yum remove flox
    ```

    We recommend rebooting your system after uninstalling Flox.


        ```
        $ sudo yum remove flox
        Updating Subscription Management repositories.
        Unable to read consumer identity

        This system is not registered to Red Hat Subscription Management.
        You can use subscription-manager to register.

        Dependencies resolved.
        ======================================================================
            Package       Architecture    Version              Repository   Size
        ======================================================================
        Removing:
            flox          x86_64          1.4.3-1625910780     @@System     109 M

        Transaction Summary
        ======================================================================
        Remove  1 Package

        Freed space: 109 M
        Is this ok [y/N]: y
        Running transaction check
        Transaction check succeeded.
        Running transaction test
        Transaction test succeeded.
        Running transaction
            Preparing        :                                               1/1
            Running scriptlet: flox-1.4.3-1625910780.x86_64                  1/1
        floxadm uninstall complete

            Erasing          : flox-1.4.3-1625910780.x86_64                  1/1
            Running scriptlet: flox-1.4.3-1625910780.x86_64                  1/1
            Verifying        : flox-1.4.3-1625910780.x86_64                  1/1
        Installed products updated.

        Removed:
            flox-1.4.3-1625910780.x86_64

        Complete!
        ```

=== "Nix - Generic"

    If you've installed flox to the system-wide `default` profile

    ``` { .text .code-command .copy }
    sudo -H nix profile remove \
            '.*flox' \
            --profile /nix/var/nix/profiles/default \
            --experimental-features "nix-command flakes"
    ```

    Or, if you've installed flox to your own _personal_ profile

    ``` { .text .code-command .copy }
    nix profile remove \
            '.*flox' \
            --experimental-features "nix-command flakes"
    ```

    Or, if you've declared Flox using a flake, remove the Flake

=== "WSL"

    Please follow the instructions provided on either the Debian or RPM tab
    (whichever matches the existing Linux Distribution installed with your
    WSL) to uninstall Flox.

[flox_discourse]: https://discourse.flox.dev

---


## Uninstall

> Source: `k8s/install/uninstall.md`

---
title: "Uninstall"
description: "Uninstalling Imageless Kubernetes from any cluster"
---

This guide describes how to remove Imageless Kubernetes from a cluster.

First, remove the `RuntimeClass` with:

```sh
kubectl delete runtimeclass flox
```

Then follow the installation-method specific guidance below.

## Amazon EKS

If a separate node group was used for Imageless Kubernetes, removing that node group and the `RuntimeClass` is all that is required to uninstall.

### Terraform

If Terraform was used to add a node group to an existing cluster:

- Remove the `eks_managed_node_group` resource from your configuration
- Apply the updated configuration

### eksctl

If `eksctl` was used, remove the node group with:

```sh
eksctl delete nodegroup -f nodegroup.yaml
```

where `nodegroup.yaml` is the file that was used to create it.

Alternatively, remove the node group directly from the AWS management console.

## Self-managed

First, remove the Flox runtime from the `containerd` configuration on each node.

The installer used in the [installation instructions][self-managed] makes a backup of the original configuration
in `/etc/containerd/config.toml.bak.xx` where `xx` is an arbitrary number.

Restore the backup with:

```sh
mv /etc/containerd/config.toml.bak.xx /etc/containerd/config.toml
systemctl restart containerd
```

Then remove the shim from each node with:

```sh
rm /usr/local/bin/containerd-shim-flox-v2
```

And finally, uninstall Flox from each node by following the instructions from the [Uninstall Flox][uninstall-flox] page.

[self-managed]: ./self-managed.md
[uninstall-flox]: ../../install-flox/uninstall.md

---


## Creating environments

> Source: `tutorials/creating-environments.md`

---
title: Creating environments
description: Reproducible environments for any project.
---

# Creating environments

You can use Flox to **set up an [environment][environment_concept]** for a new
or existing project.
Flox environments can either be activated in a new sub-shell or within the
current shell,
and they provide dependencies that take precedence over dependencies you may
have installed on your system.
Your existing dependencies are not modified in any way.
When you leave the Flox environment everything will return to its original
state.

This guide uses an `example-project` but you can follow along in your own
projects as well.

## Initialize a project

Let's set up a project called `example-project` using the
[`flox init`][flox_init] command:

```console
$ git init example-project && cd example-project
Initialized empty Git repository in /Users/your-username/example-project/.git/
```

```console
$ flox init
✨ Created environment example-project (aarch64-darwin)

Next:
  $ flox search <package>    <- Search for a package
  $ flox install <package>   <- Install a package into an environment
  $ flox activate            <- Enter the environment
```

Once an [environment][environment_concept] has been created,
you will notice some files have appeared in a `.flox` directory wherever you ran
[`flox init`][flox_init].
This is where an environment's declarative configuration is stored by default,
and can be checked into version control.

## Search, show, and install packages

We have an environment,
but it's empty.
Flox has over 80,000 open source and licensable packages to install in your
environment.
Search for and install packages using [`flox search`][flox_search],
[`flox show`][flox_show], and [`flox install`][flox_install].

Let's assume `example-project` is a nodejs/npm project.
Begin by searching for `nodejs` with [`flox search`][flox_search] in Flox:

```console
$ flox search nodejs
nodejs              Event-driven I/O framework for the V8 JavaScript engine
nodejs_20           Event-driven I/O framework for the V8 JavaScript engine
nodejs_latest       Event-driven I/O framework for the V8 JavaScript engine
nodejs-18_x         Event-driven I/O framework for the V8 JavaScript engine
nodejs_18           Event-driven I/O framework for the V8 JavaScript engine
nodejs-16_x         Event-driven I/O framework for the V8 JavaScript engine
nodejs_16           Event-driven I/O framework for the V8 JavaScript engine
nodejs-14_x         Event-driven I/O framework for the V8 JavaScript engine
nodejs_14           Event-driven I/O framework for the V8 JavaScript engine

Showing 10 of 30 results. Use 'flox search nodejs --all' to see the full list.
Use 'flox show <package>' to see available versions
```

    Don't see what you're looking for? Try `flox search <search-term> --all`.
    Still missing? Reach out to us on our [forum][discourse] for assistance.

For more detail about a specific package, such as the available versions,
use [`flox show`][flox_show].

Here we're showing nodejs:

```console
$ flox show nodejs
nodejs - Event-driven I/O framework for the V8 JavaScript engine
    nodejs@18.18.2
    nodejs@18.18.0
    nodejs@18.17.1
    nodejs@18.16.1
    nodejs@18.9.0
    nodejs@18.7.0
    ...
```

Once you've found the right package, you can install it with
[`flox install`][flox_install].

```console
$ flox install nodejs
✅ 'nodejs' installed to environment example-project at /Users/myuser/example-project
```

    Flox will warn you if you install a package that requires licensing.
    Ensure you have a license for the package before using it with Flox.

In addition to applications, let's **install system dependencies** that nodejs
may need,
such as a certificate generator.

```console
$ flox search mkcert
mkcert  A simple tool for making locally-trusted development certificates

Use `flox show <package>` to see available versions
```

```console
$ flox install mkcert
✅ 'mkcert' installed to environment example-project at /Users/myuser/example-project
```

## Enter and use the environment

Now we need to activate the environment with the
[`flox activate`][flox_activate] command to make the packages we installed
available.
When an environment is activated,
you will see your terminal's prompt change.
This example demonstrates that the packages are now available by running
`which node` and `which mkcert`.

``` {.sh .copy }
flox activate
```

```console
flox [example-project] $ which node
/Users/myuser/example-project/.flox/run/aarch64-darwin.flox/bin/node
```

```console
flox [example-project] $ which mkcert
/Users/myuser/example-project/.flox/run/aarch64-darwin.flox/bin/mkcert
```

    Some terminal themes may override Flox's terminal prompt changes.
    You will still be able to activate and use the environment.

## Customize the shell hook and environment variables

The activation process of your Flox environment can be
customized by editing the [environment's declarative manifest][manifest_concept]
with [`flox edit`][flox_edit].
This is useful for doing environment initialization,
safely working with secrets,
printing instructions for other developers,
and more.

Let's add a simple instruction to `example-project`'s environment.
To interactively edit and validate your environment,
use Flox's built-in edit function which uses your default terminal `$EDITOR`:

```console
flox [example-project] $ flox edit
```

From within the editor,
add a custom activation script under the `[hook]` block:

```toml title="manifest.toml"
# List packages you wish to install in your environment under
# the `[install]` table
[install]
nodejs.pkg-path = "nodejs"
mkcert.pkg-path = "mkcert"
# hello.pkg-path = "hello"
# nodejs = { version = "^18.4.2", pkg-path = "nodejs_18" }

# Set an environment variable. These variables may not reference once another.
[vars]
# message = "Howdy"
# pass-in = "$some-env-var"

# Set your activation hook ( run when entering the environment )
# You can write this inline with the `on-activate` field.
[hook]
on-activate = """
  echo ""
  echo "Start the server with 'npm start'"
  echo ""
"""
```

Save changes to the file.

    Edits made with [`flox edit`][flox_edit] will be validated and built
    immediately.
    Edits made to the [manifest][manifest_concept] with external software like
    an IDE will be validated when you run [`flox activate`][flox_activate].

Test out the new shell hook by running `exit` and
[`flox activate`][flox_activate] again:

```console
flox [example-project] $ exit
```

```console
$ flox activate

Start the server with 'npm start'

flox [example-project] $
```

## Exit the environment

We're done!
To exit the last [environment][environment_concept] activated,
use the `exit` command or the shell shortcut, `CTRL + D`.

```console
flox [example-project] $ exit
$
```

[flox_init]: ../man/flox-init.md
[flox_search]: ../man/flox-search.md
[flox_show]: ../man/flox-show.md
[flox_install]: ../man/flox-install.md
[discourse]: https://discourse.floxdev.com/
[flox_activate]: ../man/flox-activate.md
[flox_edit]: ../man/flox-edit.md
[sharing_guide]: ./sharing-environments.md
[layering_guide]: ./layering-multiple-environments.md
[manifest_concept]: ../concepts/environments.md#manifesttoml
[environment_concept]: ../concepts/environments.md
[customizing_guide]: ./customizing-environments.md

## Where to next?

- :simple-readme:{ .flox-purple .flox-heart } [Sharing environments][sharing_guide]

- :simple-readme:{ .flox-purple .flox-heart } [Layering multiple environments][layering_guide]

- :simple-readme:{ .flox-purple .flox-heart } [Customizing the shell hook][customizing_guide]

---


## Customizing the shell environment

> Source: `tutorials/customizing-environments.md`

---
title: Customizing the shell environment
description: Using setup scripts, aliases, and environment variables to improve your workflows.
---

# Customizing the shell environment

Activating a Flox [environment][environment_concept] places you into a subshell.
You likely already have some customizations built into your shell from your shell's configuration (`.bashrc`, `.zshrc`, `config.fish`, etc), but it can be convenient to further customize your shell based on the project that you're working on.
This guide will walk you through leveraging various features of a Flox environment to improve your quality of life when developing a Rust project, but many of the ideas are applicable to other languages as well.

## Setup

Let's assume you have a Rust project that you regularly work on.
To do that work you would already have `cargo`, `rustc`, and a few other tools installed.
For more details on what it looks like to develop in Rust with Flox, see the [Rust language guide][rust_guide].

If you'd like to follow along with a real Flox environment, create an environment via [`flox init`][flox_init] and install the tools as shown below:

```{ .bash .copy }
mkdir mycli;
cd mycli;
flox init;
flox install rustc cargo libiconv
```

Then generate a basic "Hello, World" program using `cargo init` inside the environment:

```{ .bash .copy }
flox activate -- cargo init --bin .
```

## Vars, hook, or profile?

When customizing your shell environment you have three basic knobs you can turn:

- The `[vars]` section
- The `hook.on-activate` script
- The `[profile]` section

The logic for deciding where a customization should go is application specific, but there are some simple guidelines you can follow.
For a full discussion of what logic to place in which section and why, see the [activation concept page][activation_concept].
Otherwise, try this:


- Are you setting an environment variable?
    - Is it a constant value?
        - If so, set it in the `[vars]` section.
        - If not, compute and `export` the variable in the `hook.on-activate` script.
- Are you sourcing a script (like activating a Python virtual environment)?
    - If so, do this in the `[profile]` section.
- Are you setting shell aliases?
    - If so, set them in the `[profile]` section.
- Are you doing general project setup actions (like creating a directory, etc)?
    - If so, do that in the `hook.on-activate` script.


## Adding a directory to PATH

It can be convenient to quickly run commands against the development build of a program you're working on.
For instance, if you're working on a command line application you might want to check that the help text is formatted properly by interactively running `mycli -h`.

In our case, when we build the application `cargo` will place the compiled program in `target/debug`:

```text
mycli/
    .flox
    Cargo.toml
    Cargo.lock
    src/
        main.rs
    target/
        debug/
            mycli
```

If we want to run commands with this newly compiled `mycli`, we can either tell `cargo` to build it (again) and then run it, or we can add `target/debug` to `PATH` so that we can run `mycli` like any other program.
This second option is more convenient, so let's see how you can tell your Flox environment to do that for you automatically.

If we follow the logic listed above, we're wanting to modify an existing environment variable (`PATH`), so we'll do this in the `hook.on-activate` script.
Modify your `hook.on-activate` script to look like this:

```toml
[hook]
on-activate = '''
    export PATH="$PWD/target/debug:$PATH"
'''
```

Now if you activate the environment and build `mycli` for the first time, you should be able to run `mycli` without needing to type out the path to it (e.g. `target/debug/mycli`):

```console
$ flox activate
...
$ cargo build
...
$ mycli
Hello, World!
```

### Why do I need to exit and re-activate?

Any time the Flox CLI detects that you've changed a section of the manifest that it can't automatically make take effect, you'll need to exit and reactivate.
For instance, when you install a new package via [`flox install`][flox_install], the CLI is able to make that immediately available to you so there's no need to exit and re-activate.

However, editing the `hook.on-activate` script has no effect on the currently activated environment because the `hook.on-activate` script is only run during the activation process (and the same goes for `[profile]`).
Similarly, editing the `[vars]` section has no effect on the currently activated environment because the `hook.on-activate` and `[profile]` scripts may rely on the values of variables in `[vars]`, so for the sake of correctness it makes sense to re-run those scripts.

## Enabling feature flags

Now let's say that you've worked on `mycli` for a while and developed some features that aren't publicly available, but can be accessed by setting certain feature flags.
A common way to enable or disable feature flags is by environment variables.
If you want to be able to test out those features during development, this sounds like a great thing for Flox to do for you automatically.

Let's say that we have feature flags `MYCLI_ENABLE_COLOR` and `MYCLI_TURBO_MODE` and they're enabled when we set them to `"1"`.

Going back to our "vars, hook, or profile" logic, we see that we're trying to set new environment variables with constant values.
This means we'll want to set these variables in the `[vars]` section.
Edit your `[vars]` section to look like this:

```toml
[vars]
MYCLI_ENABLE_COLOR="1"
MYCLI_TURBO_MODE="1"
```

If you're currently in the environment, exit it and activate it again for the changes to take effect, otherwise you can simply activate the environment.
In the activated environment you should now see that these two variables are set:

```console
$ flox activate
...
$ echo $MYCLI_TURBO_MODE
1
```

## Adding shell aliases

Now let's say that you'd like to use `mycli` from anywhere on your system.
Let's also say that you have a `$HOME/bin` directory that you add to `PATH` in your shell's config file.
You might use this as a place to put programs you've compiled yourself that you want to be able to run from anywhere.
We're going to create an alias for your developer environment that will build `mycli` and copy it to this directory so that it's quick and easy to install `mycli` after completing a feature you've been working on.

Going back to our "vars, hook, or profile" logic, we see that we're creating a shell alias.
This means that we'll be adding it to the `[profile]` section.
However, the syntax for defining shell aliases is shell-specific, so we'll need to declare this alias in the subsection that corresponds to our shell.
For this tutorial we'll assume that you're an enlightened [fish shell][fish_shell] user, meaning that we'll edit our `profile.fish` script.

We'll call this alias `install-bin` and it will build `mycli` in "release" mode, i.e. with full optimizations so it runs as fast as possible.
Edit your `[profile]` section to look like this:

```toml
[profile]
fish = '''
    alias install-bin "cargo build --release && cp $PWD/target/release/mycli $HOME/bin/mycli"
'''
```

Again, if you're currently in the environment, exit it.
If you want to test this alias you'll also want to create the `$HOME/bin` directory.
Now if you activate the environment and run `install-bin` you should find a copy of `mycli` in `$HOME/bin`:

```console
$ flox activate
...
$ install-bin
...
$ ls $HOME/bin
mycli
```

## Where to next?

- :simple-readme:{ .flox-purple .flox-heart } [Multiple architecture environments][multi-arch-guide]

[environment_concept]: ../concepts/environments.md
[flox_activate]: ../man/flox-activate.md
[multi-arch-guide]: ./multi-arch-environments.md
[rust_guide]: ../languages/rust.md
[flox_init]: ../man/flox-init.md
[activation_concept]: ../concepts/activation.md
[fish_shell]: https://fishshell.com/
[flox_install]: ../man/flox-install.md

---


## What is a Flox environment?

> Source: `concepts/environments.md`

---
title: What is a Flox environment?
description: Everything you need to know about Flox environments.
---

# What is a Flox environment?

An environment is a shell that provides a collection of
**environment variables**, **software packages**, and **activation scripts** that
are run when entering the shell.
Environments provide packages that take precedence over your existing packages
without removing access to personalizations not provided by the environment.
Flox environments layer on top of your system so that you can use the
environment's software when it's active,
while still using your personal shell aliases, IDE, tools, and
kitted out text editor.

See the [creating an environment guide][create_guide] to create your first
environment.

## Environment uses

1. **Path environment**: An environment stored in a local directory.
    - This environment is self contained in the `.flox` directory and can be
reproduced by sharing the directory in version control or some other file
sharing mechanism.
    - Path environments are created with [`flox init`][flox_init],
referred to with the `--dir/-d` option on most CLI commands,
and are commonly used for self-contained projects or different subprojects
within a monorepo.

2. **Centrally managed environment**: An environment stored remotely on
[FloxHub][floxhub_concept].

    - Centrally managed environments are created by running [`flox push`][flox_push]
on a path environment.
     You can connect a new project directory with an existing centrally managed environment with [`flox pull ...`][flox_pull] or you can activate the environment directly with [`flox activate -r ...`][flox_activate] (which uses a local cached copy) for instant use.
    - Centrally managed environments enable multiple projects or systems to consume a
shared environment that is versioned with [generations][generation_concept].
They are commonly used as base environments for projects of similar tech stacks,
for reproducing issues on specific systems, or to quickly share tools.
    - To disconnect a centrally managed environment from FloxHub, run [`flox pull --copy`][flox_pull] instead of `flox pull`.
    This will turn the environment back into a path environment.

See the [sharing guide][sharing_guide] for a more thorough walk through about
sharing and working with different types of environments.

## Environment files

A Flox environment stores its metadata, declarative manifest, and manifest lock
file in a `.flox` directory wherever the [`flox init`][flox_init] command was
run.
All of these files can be stored in version control when working with path environments.

Let's look closer at the files that were generated.

### `manifest.toml`

The manifest is a declarative specification for the environment which is [TOML][toml_spec] formatted.

The best way to edit the manifest is by running [`flox edit`][flox_edit] which will launch your default editor and run validation when you save changes.

See [`manifest.toml`][manifest] for a complete description of the manifest format and the [customizing environments guide][customizing_environments_guide] to walk through examples.

```toml title=".flox/env/manifest.toml"
version  = 1

[install]
nodejs.pkg-path = "nodejs_24"
```

### `manifest.lock`

The lock file serves as a snapshot of the specific package versions and their dependencies that were built and activated at a particular point in time.
Flox manages this file for you.

```json title=".flox/env/manifest.lock"
{
  …
  "packages": [
    {
      "install_id": "nodejs",
      "version": "24.0.1",
      "system": "aarch64-darwin",
      "outputs": {
        "dev": "/nix/store/by9av8x8vmk8lpw4cxhhxfbf7s1h4xzx-nodejs-24.0.1-dev",
        "libv8": "/nix/store/li49fpxxlgzaz20sahhfj6n8cbkqi7m1-nodejs-24.0.1-libv8",
        "out": "/nix/store/naafq480zhq05xbi2d3kzpnna2rdqsfb-nodejs-24.0.1"
      },
      …
    }
  …
  ]
}
```

### `pkgs`

[Nix expression builds][nix-expression-builds-concept] are stored in the directory `.flox/pkgs`.

### `env.json`

A metadata file that contains the name of the environment and the environment's
version. Flox manages this file for you.

```json title=".flox/env.json"
{
  "name": "example-project",
  "version": 1
}
```

[flox_init]: ../man/flox-init.md
[flox_show]: ../man/flox-show.md
[flox_edit]: ../man/flox-edit.md
[flox_install]: ../man/flox-install.md
[flox_search]: ../man/flox-search.md
[flox_edit]: ../man/flox-edit.md
[flox_push]: ../man/flox-push.md
[flox_pull]: ../man/flox-pull.md
[flox_activate]: ../man/flox-activate.md
[sharing_guide]: ../tutorials/sharing-environments.md
[create_guide]: ../tutorials/creating-environments.md
[customizing_environments_guide]: ../tutorials/customizing-environments.md
[generation_concept]: ./generations.md
[floxhub_concept]: ./floxhub.md
[discourse]: https://discourse.flox.dev/
[manifest]: ../man/manifest.toml.md
[nix-expression-builds-concept]: ./nix-expression-builds.md
[toml_spec]: https://toml.io/en/v1.0.0

---


## Floxhub Environments

> Source: `concepts/floxhub-environments.md`

---
title: "FloxHub environments"
description: "Reusable environments that are centrally managed on FloxHub"
---

A FloxHub environment allows you to centrally manage a Flox environment, tracking changes made to it and allowing the environment to be reused in multiple contexts.

## Background

When you create an environment for your project, you often do so via the [`flox init`][flox-init] command, which creates a `.flox` directory that you can check into source control.

```{ .sh .copy}
flox init
git add .flox
```

This allows you to track changes to the environment the same way that you track changes to your source code, but it also ties this environment to this specific project and Git repository.

Another way of working is to [push][flox-push] an environment to [FloxHub][floxhub] to turn it into a reusable, centrally managed environment.

```{ .sh }
$ flox push
✅ Updates to myenv successfully pushed to FloxHub

View the environment at: https://hub.flox.dev/myuser/myenv
Use this environment from another machine: 'flox activate -r myuser/myenv'
Make a copy of this environment: 'flox pull myuser/myenv'
```

Once pushed, the state and history of this environment are tracked on FloxHub in the form of [generations][generations].
Let's explore how FloxHub environments work and the kinds of workflows they enable.

[flox-init]: ../man/flox-init.md
[flox-push]: ../man/flox-push.md
[floxhub]: ./floxhub.md
[generations]: ./generations.md

## Terminology

We call an environment that has been pushed to FloxHub a **"FloxHub environment"**.
One of the primary benefits of FloxHub environments is that they can be reused in different contexts, by different people, on different machines.

This means you frequently have multiple copies of the environment:

- The copy that lives on FloxHub, which is the source of truth
- The copy that exists locally for a given user on a given machine

We call the copy of the environment on FloxHub the **"upstream"** copy, and the copy on a user's machine the **"local"** copy.

## Getting a FloxHub environment

Once you've pushed an environment to FloxHub, you can then use the [`flox pull`][flox-pull] command to fetch a copy of the environment to your machine.

A FloxHub environment can exist on your machine in two different forms:


- A cached copy transparently managed by Flox
    - Fetch this manually via `flox pull --reference <owner>/<name>`
- Materialized into a user-specified directory
    - Created via `flox pull <owner>/<name>`
    - Placed into the current directory by default
    - Specify a different directory with the `-d/--directory` flag


This cached copy is created and managed by the Flox CLI.
Additionally, the Flox CLI will automatically fetch updates from FloxHub (without automatically applying them) so that the locally cached copy of the environment has up to date knowledge of the upstream state.

The upstream state of the environment can be fetched manually via the `flox pull (-r | --reference) <owner>/<name>` command.

## Operations on FloxHub environments

CLI commands that interact with FloxHub environments will primarily operate on the cached copy of the environment.
This allows you to use FloxHub environments offline if a cached copy exists.

As an example, installing a package via [`flox install -r`][flox-install] will operate on the local copy, creating a new [generation][generations] of the local copy.
The Flox CLI indicates when an operation has been performed on the local copy (note the `(local)` text in the example below).

```text
$ flox install -r myuser/myenv ripgrep
✅ 'ripgrep' installed to environment 'myuser/myenv' (local)
```

When the Flox CLI detects that the local and upstream copies are out of sync (for example, you have a new local generation corresponding to the new package you installed), it will notify you with instructions on how to proceed.
For the example above, you would see the following output when activating the environment:

```text
$ flox activate -r myuser/myenv
ℹ️  Environment out of sync with FloxHub.

Local:

 * myuser installed package 'ripgrep (ripgrep)' on mymachine
   Generation:  2
   Timestamp: 2025-12-15 21:04:27 UTC

Remote:

 * myuser imported environment on mymachine
   Generation:  1
   Timestamp: 2025-12-15 18:57:23 UTC

Use 'flox push|pull -r myuser/myenv' to fetch updates or update the environment on FloxHub.

✅ You are now using the environment 'myuser/myenv (local)'.
To stop using this environment, type 'exit'
```

The `flox activate` command succeeds, but the message indicates that you need to run either a `flox pull` or `flox push` command (`flox push` in this case since you have local changes) to synchronize the two copies:

```text
Use 'flox push|pull -r myuser/myenv' to fetch updates or update the environment on FloxHub.
```

Running the `flox push` command syncs local changes to the upstream copy on FloxHub:

```text
$ flox push -r myuser/myenv
✅ Updates to myenv successfully pushed to FloxHub

View the environment at: https://hub.flox.dev/myuser/myenv
Use this environment from another machine: 'flox activate -r myuser/myenv'
Make a copy of this environment: 'flox pull myuser/myenv'
```

[flox-pull]: ../man/flox-pull.md
[flox-install]: ../man/flox-install.md

## Getting information from upstream

### Generations

Both the local and upstream FloxHub environments track their state over time via generations.
For an in-depth explanation of generations, see the [Generations][generations] concept page.

In order to view the list of generations as understood by the local copy, you use the [`flox generations list`][gen-list] command.
To see the list of generations as understood by the upstream copy, you add the `--upstream` flag.

In order to view the _history_ of generations (which displays how the "live" generation has evolved over time, any rollbacks that occurred, etc), you use [`flox generations history`][gen-hist].
Again, the `--upstream` flag will show you the history as understood by the upstream copy.

### Packages

In order to see the list of packages in the local copy of a FloxHub environment you use the [`flox list -r`][flox-list] command.
Add the `--upstream` flag to see the packages in the upstream copy of the FloxHub environment.

[gen-list]: ../man/flox-generations-list.md
[gen-hist]: ../man/flox-generations-history.md
[flox-list]: ../man/flox-list.md

## Activating a FloxHub environment

Activating a FloxHub environment is done via the [`flox activate -r`][flox-activate] command.
This will activate the current state of the local copy of the FloxHub environment, which may not be up to date with the upstream copy.
To activate the environment as it exists upstream, run `flox pull -r <owner>/<name>` before running `flox activate -r`.

[flox-activate]: ../man/flox-activate.md

---


## Layering multiple environments

> Source: `tutorials/layering-multiple-environments.md`

---
title: Layering multiple environments
description: Using more than one environment at a time
---

# Layering multiple environments

This guide walks you through layering a [`default`][default-env] environment
with a project's environment.

## Create your default `$HOME` environment

First, create your `default` environment by following
[`default` environment tutorial][default-env].

## Install packages

Now lets [`flox install`][flox_install] **tools that will be useful on any
system** regardless of the project.
Here we are installing `curl`, `gitFull`, `gnupg`, `inetutils`, `tree`, and
`vim`.

```console
$ flox install curl gitFull gnupg inetutils tree vim
✅ 'curl' installed to environment default at /Users/youruser
✅ 'gitFull' installed to environment default at /Users/youruser
✅ 'gnupg' installed to environment default at /Users/youruser
✅ 'inetutils' installed to environment default at /Users/youruser
✅ 'tree' installed to environment default at /Users/youruser
✅ 'vim' installed to environment default at /Users/youruser
```

Let's inspect the contents of the environment with [`flox list`][flox_list]:

```console
$ flox list
curl: curl (8.4.0)
gitFull: gitFull (2.42.0)
gnupg: gnupg (2.4.1)
inetutils: inetutils (2.5)
tree: tree (2.1.1)
vim: vim (9.0.2116)
```

We can test the environment is working properly with
[`flox activate`][flox_activate].

```console
$ flox activate
flox [default] $ which git
/Users/youruser/.flox/run/aarch64-darwin.default/bin/git
flox [default] $ git --version
git version 2.42.0
```

Everything is working!

## Layering a project environment

Now that we have our tools in the `default` environment we can layer on a new
environment that brings in project-specific dependencies.
For this example we will use a publicly accessible Node project called
`material-ui`.

Let's clone the example project to our home directory and enter the project's
directory:

```console
flox [default] $ git clone https://github.com/mui/material-ui.git
Cloning into ...
flox [default] $ cd material-ui
```

Use [`flox init`][flox_init] from the `material-ui` directory that we are in.

```console
flox [default] $ flox init
✨ Created environment material-ui (aarch64-darwin)

Next:
  $ flox search <package>    <- Search for a package
  $ flox install <package>   <- Install a package into an environment
  $ flox activate            <- Enter the environment
```

This project only requires `yarn` so let's install it with
[`flox install`][flox_install].

```console
flox [default] $ flox install yarn
✅ 'yarn' installed to environment material-ui at /Users/youruser/material-ui
```

Now we're ready to do development on this project!
Let's activate the `material-ui` Flox environment and start `material-ui`'s
development server.

```console
flox [default] $ flox activate
flox [material-ui default] $ yarn start
...
```

We now have access to both the dependency this project needs (`yarn`) and the
tools we need to do development on any project (`vim`, `git`, etc)!
You can layer as many environments as you want.
If two environments contain the same package,
Flox will use the package from the last environment activated.

You can use `flox envs` to see the environments you have activated.

```console
$ flox envs
✨ Active environments:
  material-ui  /home/youruser/material-ui
  default      /home/youruser

Inactive environments:
```

## Where to next

- :simple-readme:{ .flox-purple .flox-heart } [Sharing environments][sharing_guide]

- :simple-readme:{ .flox-purple .flox-heart } [Customizing the shell hook][customizing_guide]

- :simple-readme:{ .flox-purple .flox-heart } [Designing multiple architecture environments][multi_arch_guide]

[default-env]: ./default-environment.md
[flox_init]: ../man/flox-init.md
[flox_install]: ../man/flox-install.md
[flox_activate]: ../man/flox-activate.md
[flox_list]: ../man/flox-list.md
[sharing_guide]: ./sharing-environments.md
[customizing_guide]: ./customizing-environments.md
[multi_arch_guide]: ./multi-arch-environments.md

---


## Designing cross-platform environments

> Source: `tutorials/multi-arch-environments.md`

---
title: Designing cross-platform environments
description: Creating environments that run on different systems.
---

# Designing cross-platform environments

Flox makes it simple to have the **same [environment][environment_concept] on
multiple systems and CPU architectures**.
This guide walks through an example between two coworkers who have different
system types,
and shows how to customize your environment with system-specific dependencies.

## Creating an environment

To get started,
let's create an [environment][environment_concept] from a Linux laptop.
This laptop is using an ARM CPU (aarch64) which makes its full system
type `aarch64-linux`.

When using [`flox search`][flox_search] you may see packages that won't immediately work with your manifest, but finding and allowing system specific packages is very easy.
Flox shows software from the following systems: `aarch64-darwin`, `x86_64-darwin`, `aarch64-linux`, and `x86_64-linux`.

Some packages may support only a subset of system types. You can inspect a
package with [`flox show`][flox_show] to see what system types are supported:

```console
$ flox show gdb
gdb - The GNU Project debugger
    gdb@14.2 (aarch64-linux, x86_64-darwin, x86_64-linux only)
    gdb@14.1 (aarch64-linux, x86_64-darwin, x86_64-linux only)
    gdb@13.2 (aarch64-linux, x86_64-darwin, x86_64-linux only)
    gdb@13.1 (aarch64-linux, x86_64-darwin, x86_64-linux only)
...
```

First let's install some packages to our environment running on Linux:

```console
$ flox init --name eng-team-tools
✨ Created environment eng-team-tools (aarch64-linux)
...
$ flox install gnupg vim
✅ 'gnupg' installed to environment eng-team-tools at /home/youruser
✅ 'vim' installed to environment eng-team-tools at /home/youruser
```

To make it easy to share this system across platforms we are going to share it
on FloxHub with [`flox push`][flox_push].

```console
$ flox push
✅  eng-team-tools successfully pushed to FloxHub

    Use 'flox pull youruser/eng-team-tools' to get this environment in any other location.
```

Learn more about this and other sharing options in the
[sharing environments guide][sharing_guide].

## Using the environment from a different system type

Many packages in Flox will work without any issue across system types.

To test this out, run [`flox pull`][flox_pull] from another system such as an
Apple machine with an M-series processor.
This system type is `aarch64-darwin`.
Then lets run the a simple `gpg --version` command to test everything is working.

```console
$ flox pull youruser/eng-team-tools
✨  Pulled youruser/eng-team-tools from https://hub.flox.dev

    You can activate this environment with 'flox activate'
$ flox activate -- gpg --version
gpg (GnuPG) 2.4.5
libgcrypt 1.10.3
Copyright (C) 2024 g10 Code GmbH
...
```

Looks like the environment works cross-platform, nice!

## Handling unsupported packages

However, some packages only work with a subset of systems.
To demonstrate this let's install a package that **isn't compatible with an Apple machine**.

From the Linux machine...

```console
$ flox install systemd
⚠️  'systemd' installed only for the following systems: aarch64-linux, x86_64-linux
```

Flox installs the package for all systems that it's compatible with,
but it skips Apple systems since they don't support the package.
We can push this update so we can list packages from the Apple machine to verify
everything works.

```console
$ flox push
✅  Updates to eng-team-tools successfully pushed to FloxHub

    Use 'flox pull youruser/eng-team-tools' to get this environment in any other location.
```

Then, from the Apple machine, let's pull the latest and inspect the manifest.

```console
$ flox pull
✅ Pulled youruser/eng-team-tools from https://hub.flox.dev/

You can activate this environment with 'flox activate'

$ flox list
gnupg: gnupg (2.4.5)
vim: vim (9.1.0377)

$ flox list -c
...
[install]
gnupg.pkg-path = "gnupg"
vim.pkg-path = "vim"
systemd.pkg-path = "systemd"
systemd.systems = ["aarch64-linux", "x86_64-linux"]
...
```

The Apple machine does not have `systemd`, because the `systemd.systems` list
specifies that `systemd` should only be installed on Linux.
This environment will activate on both machines and the Apple machine won't
get the `systemd` package.

## Where to next?

- :simple-readme:{ .flox-purple .flox-heart } [Environment concept][environment_concept]

[environment_concept]: ../concepts/environments.md
[sharing_guide]: ./sharing-environments.md
[flox_search]: ../man/flox-search.md
[flox_show]: ../man/flox-show.md
[flox_edit]: ../man/flox-edit.md
[flox_push]: ../man/flox-push.md
[flox_pull]: ../man/flox-pull.md

---


## Sharing your environments

> Source: `tutorials/sharing-environments.md`

---
title: Sharing your environments
description: Multiple ways to share your environment with others.
---

# Sharing your environments

Flox provides **three main ways of sharing environments** with others:

- **Sharing environments with files:**: Flox environments are shared via the `.flox` folder and often checked into version control.
- **Sharing environments on FloxHub**: Flox environments are shared via FloxHub and available to all `flox` commands with `-r username/environment`. Commands operate on your local copy; use `flox push` to sync changes to FloxHub.
- **Containers**: Flox environments are used to create container images.

## Sharing environments with files

New [environments][environment_concept] created with [`flox init`][flox_init] will create a `.flox` folder in the directory where [`flox init`][flox_init] was run. This folder contains everything required to run this environment on their system and can be sent to another user any way files are shared. It is most common to commit the `.flox` to a version controlled code repository such as git. If shared this way, the user needs only `git clone` the project and `flox activate` in the directory containing the `.flox`.

    If you are sharing an environment with a user on a different CPU architecture or OS from the person who created the environment, you may run into some issues where system-specific packages are not available on their OS. This can be fixed with a minor edit to the manifest, described in the [manifest concept][manifest_concept]. If you get stumped, reach out to us on our [forum][discourse] for assistance.

Here is an example of sharing a project with files. The first person creates the environment:

```console
$ mkdir example-project # (1)!
$ cd example-project
$ git init
...
$ flox init
...
```

1. `example-project` is a stand-in for a git source code managed project.

Install packages:

```console
$ flox install nodejs mkcert
✅ 'nodejs' installed to environment example-project at /Users/youruser/example-project
✅ 'mkcert' installed to environment example-project at /Users/youruser/example-project
```

Add the `.flox` directory and commit the changes.

```{ .sh .copy }
git add .flox;
git commit -m "sharing flox environment"
```

Another developer on the same project can get started immediately with [`flox activate`][flox_activate], which will automatically download the same versions of those packages to their machine:

```{ .sh .copy }
git clone ..example-project;
flox activate
```

[flox_init]: ../man/flox-init.md
[discourse]: https://discourse.flox.dev/
[manifest_concept]: ../concepts/environments.md#manifesttoml

## Sharing environments on FloxHub

Instead of sharing environments with files, you can share them on
[FloxHub][floxhub_concept] with a free account, which eliminates the need to
clone a repository when using the environment.

Once an environment has been pushed to FloxHub, it can be used in number of
different workflows:

- You can `flox pull --copy` an environment to [use it as a template for a new project](composition.md#creating-a-template-for-new-projects).
- You can use it directly in other environments by [adding it to another environment's `[include]` section](composition.md#composing-environments).
- You can use it to share software across multiple machines, most commonly with a default environment, by [adding it to your terminal's RC files](default-environment.md#initial-setup).
- Finally, you can use it to materialize an ad-hoc set of tools, which we'll show here.

To create an environment on FloxHub, first use `flox init` to create it locally:

```console
$ mkdir llm_tools
$ cd llm_tools
$ flox init
$ flox install codex gemini-cli
✅ 'codex' installed to environment llm_tools at /Users/youruser/llm_tools
✅ 'gemini-cli' installed to environment llm_tools at /Users/youruser/llm_tools
```

Then push it:

```console
$ flox push
✅  llm_tools successfully pushed to FloxHub

    Use 'flox pull youruser/llm_tools' to get this environment in any other location.
```

You can also view your new environment on FloxHub.

### Using a local copy of a FloxHub environment

Suppose you've dropped into a shell on another host or in a container, and you need to use a tool not on that host.
To activate your FloxHub environment, run:

```console
$ flox activate -r youruser/llm_tools
✅ You are now using the environment 'llm_tools'
To stop using this environment, type 'exit'
$ # ask gemini a question
```

This will implicitly pull the environment and create a local copy of the environment if it doesn't already exist.

### Pulling a FloxHub environment into a directory (and pushing updates)

If you intend to commit the environment to version control, you may want to [`flox pull`][flox_pull] it instead.

[`flox pull`][flox_pull] adds a `.flox` folder to the directory you are in that is linked to the FloxHub environment. When using a [FloxHub][floxhub_concept] environment in multiple projects it allows centralized management of the dependencies used across these projects. Run `flox pull` to sync the latest changes from FloxHub:

```console
$ cd similar-example-project
$ flox pull youruser/example-project
✨  Pulled youruser/example-project from https://hub.flox.dev

    You can activate this environment with 'flox activate'
```

After pulling an environment you can install changes to it locally and, when you're ready, [`flox push`][flox_push] them to FloxHub if you have permissions:

```console
$ flox install yarn
✅ 'yarn' installed to environment youruser/example-project at /Users/youruser/similar-example-project
$ flox push
✅  Updates to example-project successfully pushed to FloxHub

    Use 'flox pull youruser/example-project' to get this environment in any other location.
```

    Right now, only environment owners can push edits to their environments.

[flox_push]: ../man/flox-push.md
[flox_pull]: ../man/flox-pull.md
[flox_activate]: ../man/flox-activate.md
[floxhub_concept]: ../concepts/floxhub.md

## Sharing with containers

Flox can render that environment as an OCI container runtime suitable for use with containerd, Docker, Kubernetes, Nomad, and more.

Let's create a container image from the `example-environment` we have been working with.

To render your environment to a container, run `flox containerize`. This command
will automatically load the image into Docker:

```console
$ flox containerize --runtime docker # (1)!
...
Creating layer 1 from paths: [...]
...
Loaded image: example-project:latest
✨ Container written to Docker runtime
```

1. See [`flox containerize`][flox_containerize] for more output options.

    By default Flox splits every dependency into a different layers, which allows
    better dependency sharing and faster iteration.

Now let's run a command from our image:

```console
$  docker run --rm -it example-project -- telnet --version
telnet (GNU inetutils) 2.5
...
```

## Where to next?

- :simple-readme:{ .flox-purple .flox-heart } [Layering multiple environments][layering_guide]

- :simple-readme:{ .flox-purple .flox-heart } [Customizing the shell hook][customizing_guide]

- :simple-readme:{ .flox-purple .flox-heart } [Designing multiple architecture environments][multi_arch_guide]

[multi_arch_guide]: ./multi-arch-environments.md
[environment_concept]: ../concepts/environments.md
[layering_guide]: ./layering-multiple-environments.md
[customizing_guide]: ./customizing-environments.md
[flox_containerize]: ../man/flox-containerize.md

---


## What is the Flox Catalog?

> Source: `concepts/packages-and-catalog.md`

---
title: What is the Flox Catalog?
description: Everything you need to know about the Flox Catalog and Packages.
---

# What is the Flox Catalog?

A Flox Catalog is a collection of package artifacts and associated metadata that can be consumed via a Flox Environment. The contents of a catalog can be searched, shown, and installed into an environment by way of the [flox search][flox_search], [flox show][flox_show], and then [flox install][flox_install] commands.

There are two types of catalogs:

The Base Catalog is populated by Flox and contains packages over time as maintained by the Nix Community by way of The [Nixpkgs](https://github.com/nixos/nixpkgs) Collection.

Custom Catalogs are maintained by the Users and Organizations that own them by way of the `flox publish` command, as described in the [Build][builds] and [Publish][publishing] concept pages.

The visibility of Custom Catalogs can be public or private, and packages from all types of catalog are consumed by way of the same flox (search|show|install) commands.

It can also be consulted on [https://hub.flox.dev/packages](https://hub.flox.dev/packages).

A **package** is a collection of computer programs and related data that are
bundled for distribution together on a UNIX-based computer system.
Packages are declared in the [environment manifest][manifest_concept].

## Base Catalog and nixpkgs

The built-in catalog is called the [Base Catalog][base_catalog], and contains a wide variety of open source packages you can use in your environments.
The Base Catalog uses [nixpkgs][nixpkgs] as an input.
Nixpkgs is a community maintained project, but the [Base Catalog][base_catalog] is maintained by Flox.
Upstream changes in [nixpkgs][nixpkgs] are reflected in the Flox Catalog daily from the `nixos-unstable` branch of [nixpkgs][nixpkgs].

## Supported package metadata

* **pkg-path**: unique location in the Flox Catalog.
* **version**: semantic version of the package.
* **license**: license metadata.
* **unfree**: indicates if the software uses a license not defined as Open
Source by the Open Source Initiative (OSI).
* **broken**: indicates if the package is marked as broken in
[nixpkgs][nixpkgs].

[base_catalog]: ./base-catalog.md
[flox_search]: ../man/flox-search.md
[flox_show]: ../man/flox-show.md
[flox_install]: ../man/flox-install.md
[flox_update]: ../man/flox-update.md
[manifest_concept]: ./environments.md#manifesttoml
[nixpkgs]: https://github.com/NixOS/nixpkgs
[builds]: ./builds.md
[publishing]: ./publishing.md

---


## Manifest Builds

> Source: `concepts/manifest-builds.md`

---
title: "Manifest Builds"
description: Manifest builds with Flox
---

See the [builds concept][builds-concept] page for an overview of the different types of builds and how to perform them.

## Overview

Manifest builds are defined in the `[build]` section of the manifest and take place in the context of an environment.
What that means is that a build run by the Flox CLI behaves similarly to activating the environment yourself and running the build commands manually.
This allows you to achieve a level of reproducibility while still being able to run the build commands you're familiar with (`cargo build`, `go build`, etc).

Builds can be performed with varying levels of rigor, or "purity", allowing you to choose for yourself which tradeoffs you want to make between effort and correctness.

In addition to ensuring that the build environment is the same as your developer environment, the Flox CLI will also perform some checks on the result of your build to determine whether there are missing dependencies.
This prevents a scenario in which your package builds without issue, but fails at runtime because a runtime dependency is missing.

All of this serves to ensure that the process of building your software is reliable, reproducible, and well understood, while at the same time providing a helping hand to ensure that your software behaves as expected at run time.

## Defining builds

Each build specified in the `[build]` section corresponds to a different package.
This allows you to produce multiple packages from a given set of sources, to produce, for example, a production build, a debug build, and an archive of the build sources all at the same time.

Configuring a build entails providing a short Bash script containing the build instructions.
This script often contains the same commands you would normally run to build the package in your shell e.g. `make`, `cargo build`, etc.
Flox runs this script inside an activation of the environment so that the tools used to develop the software are available during the build.
You can optionally define a `version` and `description` for the package to provide metadata used during the [publish][publish-concept] process.
See the [build section of the manifest reference][manifest-reference] for more details on the available options.

An example build definition for a Rust project called `myproject` looks like this:

```toml
[build.myproject]
command = '''
  cargo build --release
  mkdir -p $out/bin
  cp target/release/myproject $out/bin/myproject
'''
version = "0.0.1"
description = "The coolest project ever"
```

Your build script can refer to other builds in the same manifest via the `${name}` syntax, where `name` is the name of another build defined in the `[build]` section of your manifest.
Builds referred to this way will be performed before the build that references them.
This allows you to perform multi-stage builds.
This is important for "pure" builds, which will be discussed shortly.

### Build outputs

To keep the output of a build separate from the source files, every build is supplied with a directory whose path is stored in a variable named `out`.
Only the files stored in this directory are considered part of the output of a build and it is empty by default.
This is why you see the following line in the build command for the `myproject` example above

```sh
mkdir -p $out/bin
cp target/release/myproject $out/bin/myproject
```

The contents of the `$out` directory should adhere to the [Filesystem Hierarchy Standard (FHS)][fhs-docs], which is just the official name for the familiar `bin`, `lib`, etc directories you may be familiar with from using Unix-based systems.

What this means in practice is:

- Executable files should be placed in `$out/bin`, `$out/sbin`, or `$out/libexec`. Executable files placed in other directories will likely not work properly. Scripts written to these directories still need to be marked as executable via `chmod +x`.
- Man pages should be placed in `$out/share/man`.
- Libraries should be placed in `$out/lib`
- Configuration should be placed in `$out/etc`.

## Pure builds

Builds can be performed with different levels of "purity", meaning different levels of access to the outside world.
This is controlled with the `sandbox` option.

By default this option is set to `"off"`, which instructs the Flox CLI to perform the build in the root of the repository with no restrictions on network or filesystem access.
This is convenient because it allows your build scripts to work as they do in your development environment, such as using local caches and intermediate build artifacts that already exist.
However, that also implies that builds can access and embed information about files (e.g. configuration in `$HOME`) or programs (e.g. system wide applications) that are specific to your machine.
This can subsequently hurt the reproducibility of the build script and the ability to run binaries on other machines where those referenced files do not exist.

When set to `sandbox = "pure"` the Flox CLI is instructed to perform the build in a clean environment.
This entails copying all files tracked by `git` into a temporary directory and running the build in a sandboxed environment that limits filesystem access to those files copied to the temporary build directory.
Sandboxed builds on Linux are also restricted from accessing the network, but the sandboxing mechanisms on macOS are somewhat limited and thus pure builds on macOS **_will still have network access_**.
This provides much stronger guarantees that the build is reproducible, but will often require some additional changes to your build scripts.

### Vendoring dependencies

Many language ecosystems rely on network access to fetch dependencies or access to a global cache of previously fetched dependencies.
Pure builds on both macOS and Linux disallow filesystem access to these global filesystem locations.
Similarly, pure builds on Linux disallow network access and thus prevent build tools from fetching dependencies or refreshing package indices.
This means that pure builds must already have all of their dependencies present in the build environment.

One way to accomplish this is with a multi-stage build where an impure build produces an output containing the vendored dependencies, and then a pure build in turn depends on that build using the `${name}` syntax in its build script to place the vendored dependencies in a location that the build tooling can understand.

Here's an abbreviated example demonstrating how to achieve this pattern with Go (see the [Go cookbook page][go-example] for more precise instructions):

```toml
[build.deps]
command = '''
  mkdir -p $out/etc
  go mod vendor -o $out/etc/vendor
'''

[build.myproject]
command = '''
  cp -r ${deps}/etc/vendor ./vendor
  go build
'''
sandbox = "pure"
```

## What can you build?

The obvious answer to this question is, of course, "software", but this omits a variety of interesting use cases that may not be immediately obvious.

At the end of the day, a "build" is just a script that runs in your activated environment and places one or more files into a directory.
Once that build is done, the package can be [published][publish-concept] so that your or anyone else in your [organization][organizations-concept] can install it into their environment.
This can be a very convenient method of distributing all kinds of files, regardless of whether they're executables or configuration files.

Sharing packages with other users is only possible with an organization.
See the [organizations][organizations-concept] page for more details on organizations.

In short, if you have a file that can be copied into the `$out` directory, it can be distributed to others in your organization with Flox.

### Example: configuration files

Say that Nginx is used as a web server throughout your organization, and there is some common configuration that you want every instance to include (e.g. always listen on the same local port, etc).
Flox environments don't allow you to package arbitrary files along with them, but a build that produces this config file can be published and then consumed by anyone with access to your private catalog.

That build would be very simple:

```toml
[build.nginx_config]
command = '''
  mkdir -p $out/etc
  cp nginx.conf $out/etc/nginx.conf
'''
```

Once this packge is published, any environment that installs it would then be able to reference the config file as `$FLOX_ENV/etc/nginx.conf`.

### Example: protocol buffers

Say that your organization uses [grpc][grpc] to communicate between services.
It's common to vendor the `.proto` files in each project's repository or store the `.proto` files in a separate, central repository for each project to refer to.
However, you could also write a build that copies these `.proto` files and publishes them as a package.
This allows you to version and attach metadata to the `.proto` files, and any team that "installs" the package would have access to them.

Furthermore, since these `.proto` files are installed as a package, any environment that installs them would be notified when there are updates available.

## Limiting the package size

Your package likely has dependencies, and those dependencies have their own dependencies, all the way down to `libc`.
We call this complete set of dependencies the "transitive closure", or simply "the closure", of your package.
A large closure for your package has no direct impact on runtime performance, but it means that your package requires more disk space to install and requires more bandwidth to copy from one place to another.

By default all of the packages in the default [package group][pkg-groups] are included as dependencies of your packages, but these packages may only be needed by your package at _build_ time or _development_ time, not _run_ time.
As a reminder, the default package group is called `toplevel`, and all packages installed to an environment without an explicit `pkg-group` are placed into this package group.

The `runtime-packages` option allows you to trim down the packages from the `toplevel` package group that are included as runtime dependencies of your package.
This option is a list of `install-id`s from the `toplevel` package group.
As a reminder, the `install-id` is the part of the package descriptor that comes before `pkg-path` e.g. `myhello` in `myhello.pkg-path = "hello"`.

Below is an example manifest that installs two packages needed for development, `hello-go` and `ripgrep`, and restricts the runtime dependencies of the build to only `hello-go` (omitting `ripgrep`):

```toml
version = 1

[install]
hello.pkg-path = "hello-go"
ripgrep.pkg-path = "ripgrep"

[build.hello-pkg]
command = '''
  mkdir -p $out/bin
  echo "hello-go" > $out/bin/hello-pkg
  chmod +x $out/bin/hello-pkg
'''
runtime-packages = [ "hello" ] # List of `install-id`s

[options]
systems = ["aarch64-darwin", "x86_64-darwin", "aarch64-linux", "x86_64-linux"]
```

Note again that we include the `install-id` `"hello"` in `runtime-packages`, not the name of the package itself (`hello-go`).

## Examples

We've compiled a list of example commands to demonstrate how to use Flox to build packages in various ecosystems.
Each language guide in the Languages section of the Cookbook contains an example of building a package with Flox.
For example, [this section][go-example] contains an example build for the Go language.

[builds-concept]: ./builds.md
[manifest-reference]: ../man/manifest.toml.md#build
[services-concept]: ./services.md
[publish-concept]: ./publishing.md
[fhs-docs]: https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
[pkg-groups]: ../man/manifest.toml.md#package-descriptors
[grpc]: https://grpc.io/
[organizations-concept]: ./organizations.md
[go-example]: ../languages/go.md#build-with-flox

---


## Services

> Source: `concepts/services.md`

---
title: Services
description: Using services with your environment
---

# Services

It is very common for software projects to depend on other programs for core
parts of their functionality.
A web service may depend on a load balancer and a database.
A developer working on the front end of a website may need a development server
running that hot-reloads the site as they tweak the CSS.
You may also want a program that automatically runs your test suite when file
changes are detected.

What these use cases all have in common is that they use long-running programs
as part of the development lifecycle,
and the developer likely wants those programs running as soon as they sit down
to start working on the project.

We call these long-running programs "services",
and you can integrate them directly with your environment.

## Defining services

Services are defined in the `[services]` section of the manifest.
Services have a very simple schema consisting of a `command` to run to start
the service,
any `vars` you want set specifically for the service,
and whether the service spawns a background process.
See [`manifest-toml(1)`](../man/manifest.toml.md) for
more details on the exact format of the `[services]` section of the manfiest.

An example service definition is shown below:

```toml
[services.database]
command = "exec postgres -D \"$PGDATA\" -p \"$PGPORT\""
vars.PGUSER = "myuser"
vars.PGPASSWORD = "super-secret"
vars.PGDATABASE = "mydb"
vars.PGPORT = "9001"
```

This definition creates a service called `database` that starts a PostgreSQL
database and configures some of its properties through environment variables.

Some services cannot be shut down by the default mechanism (sending the spawned process a `SIGTERM`).
Most often this is because the spawned process itself spawns another process (typically a daemon) and then terminates. In this case you need to provide your own command for shutting down the service. You do this by setting `is-daemon = true` for the service and providing a `shutdown.command`. Below is an example that uses `pg_ctl` (the daemon-spawning launcher) instead of `exec postgres`, which launches postgres in the foreground. It demonstrates the `is-daemon = true` + `shutdown.command` pattern for programs that background themselves. Together these fields allow the service manager to shut down services that background themselves.

```toml
command = "pg_ctl start -D \"$PGDATA\" -l \"$PGDATA/server.log\" -o \"-p $PGPORT\""
is-daemon = true
shutdown.command = "pg_ctl stop -D \"$PGDATA\" -m fast"
vars.PGUSER = "myuser"
vars.PGPASSWORD = "super-secret"
vars.PGDATABASE = "mydb"
vars.PGPORT = "9001"
```

You can define a `shutdown.command` for any service, including services that do not run as daemons. Note that this pattern can have unpredictable effects in practice: it replaces the Flox service manager’s controlled `SIGTERM` → grace → `SIGKILL` shutdown path, which tracks the service’s PID, with the command that you define. And if your shutdown command fails to locate and kill the process for any reason, there's no fallback; the service never receives any signal and keeps running.

## Starting services

Services can be started automatically when you activate your environment via
the `flox activate --start-services` command
(or via the shorter `flox activate -s`).
This will start services as part of activating your environment.
When activating your environment from multiple shells you only need to start
the services once.
Since your services are just processes running on your machine,
they will be visible to any other activations.

Activating your environment without the `--start-services` flag will not start
the services.
If you activate your environment without services and then later decide that
you want to start them, that is done via the `flox services start` command.
When called without any arguments this command will start all services listed
in the manifest.
You can also specify individual service names,
in which case only those services will be started.
If you accidentally provide a service name that doesn't exist,
you'll get an error and no services will be started.
If a service is already running,
you'll see a warning but the command will otherwise succeed.

## Stopping services

Services are **automatically stopped** when the last running activation of the
environment terminates.
This means that if you `flox activate -s` in a single shell,
the services will be shut down automatically when you exit that shell.
Similarly, if you `flox activate -s` in one shell, then `flox activate` in two
more shells,
the services won't be shut down until all three of those activations have
terminated.

You can stop services yourself via the `flox services stop` command.
You can also specify individual service names,
in which case only those services will be stopped.
If you accidentally provide a service name that doesn't exist,
you'll get an error and no services will be stopped.
If a service is already stopped,
you'll see a warning but the command will otherwise succeed.

## Restarting services

Services can be restarted via the `flox services restart` command.
You can also specify individual service names,
in which case only those services will be restarted.
If you accidentally provide a service name that doesn't exist,
you'll get an error and no services will be restarted.

## Handling environment edits

While working in your environment that has running services,
you may discover that you need to edit a service definition or some other part
of the environment.
In this scenario you would call `flox edit` like usual,
but now the manifest is out of sync with both the current activation of your
environment _and_ the running services.
After making the edit you'll see a warning about needing to reactivate your
environment in order to apply the changes to your shell,
but if you just want to apply the changes to your services
(say you only modified a service definition)
you can do so without needing to reactivate your environment.

There are two ways to accomplish this:

1. `flox services restart`
2. `flox services stop` followed by `flox services start`

In both cases the services will be started in an ephemeral activation so that
the services can be started in the same environment as they otherwise would be
in a new activation.
The `flox services stop` in the second case is only necessary if any services
are currently running.

## Checking on services

You can see the status of your services with the `flox services status`
command.
This will display the name of the service, the PID, and its status.
An example is shown below:

```console
NAME       STATUS            PID
database   Running         12345
server     Running         23456
```

You can see the logs of your services with the `flox services logs` command.
This command operates in two modes:

- all services with `--follow`
- single service with either `--follow` or `--tail`

When no services are specified the `--follow` flag must be provided,
in which case logs for all running services will be displayed in real time.
If a single service name is provided then the logs for that service will be
displayed.

Logs for the service manager itself are stored as `services.*.log` files in the
`.flox/logs` directory of your environment.

---


## Troubleshooting

> Source: `k8s/install/troubleshooting.md`

---
title: "Troubleshooting"
description: "Troubleshooting Imageless Kubernetes installation"
---

This guide describes possible issues and solutions that may arise during the installation of Imageless Kubernetes.

## Pods stuck in `ContainerCreating`

If your pods are stuck in the `ContainerCreating` state with a message like `no runtime for "flox" is configured`, the shim installation may have been disrupted or failed.

### Configuration conflicts

The Flox additions to `/etc/containerd/config.toml` may be getting overridden by competing entries in an imported configuration file.

Verify the Flox runtime configuration is present in the active containerd config:

1. Dump the active containerd configuration and verify the Flox runtime is present:

    ```bash
    containerd config dump | grep -A 10 "flox"
    ```

2. Check if `containerd config dump` has an `imports` section that might be loading other configuration files.

3. Confirm the relevant sections exist in the output:

    ```toml
    [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.flox]
        runtime_path = "/usr/local/bin/containerd-shim-flox-v2"
        runtime_type = "io.containerd.runc.v2"
        pod_annotations = [ "flox.dev/*" ]
        container_annotations = [ "flox.dev/*" ]
    [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.flox.options]
        SystemdCgroup = true
    ```

4. If the configuration is missing or incorrect, and an `imports` section is present, you may need to manually add the Flox runtime section to the competing imported file and restart `containerd`.

    This scenario is more likely if the NVIDIA Container Toolkit is installed on the same node as Imageless Kubernetes.

### EKS node shim installation failure

The Flox `containerd` shim may have failed to install properly on the EC2 instance during setup.

Check the system logs in the EC2 console to identify any errors:

1. Navigate to the EC2 console and select your instance.
2. Click **Actions** → **Monitor and troubleshoot** → **Get system log**.
3. Review the logs for any errors related to containerd or the Flox shim installation.

---


## Activating environments

> Source: `concepts/activation.md`

---
title: Activating environments
description: How an environment is activated, and how to make the most of it
---

# Activating environments

[Environments][environment-concept] are a central concept in Flox,
representing the tools you want to use, all of their dependencies,
various environment variables necessary to make them function properly,
_and_ all of your customizations.
Given that environments are such an important part of Flox,
it stands to reason that _how you use them_ is also an important part of Flox.

There are four different ways to use an environment,
and two different modes that an environment can be activated in.
At the end of the day, though, it all boils down to properly configuring a
shell.
The `hook` and `profile` scripts specified in your manifest are run as part of
configuring that shell.
Understanding when and why they're run will help you take full advantage
of Flox,
so let's walk through what it means to "activate" an environment and how it
works.

## Configuring the shell

When you "activate" an environment,
Flox configures a shell,
making all of the packages and environment variables specified in your
manifest available, as mentioned above.

The most basic way to activate an environment is simply by calling
`flox activate`,
which puts you into a subshell with everything configured:

```{ .console .no-copy }
$ flox activate
flox [myenv] $ # Now you can use your packages
```

One of the core features that makes Flox so attractive for development is that
the packages in your manifest are available when the environment is active,
and they're gone when it's inactive.
We do this by carefully setting a collection of environment variables,
some of which you may be familiar with, such as `PATH`, and others which you
may not have heard of like `ACLOCAL_PATH`, `RUST_SRC_PATH`, and others.

As an example, if you create an environment `myenv` and install `hello`,
Flox will place `<path to myenv>/.flox/run/<your system>.myenv.dev/bin` at the
beginning of your `PATH` variable so that `hello` will be selected from your
environment rather than from elsewhere on your system.

## Four different ways to activate

We mentioned above that there are four different ways to use an environment.

### Subshell

We've already mentioned the first method,
which is to put you into a subshell.
When you activate this way your existing shell is paused and you're put into a
new one configured by Flox.
Once this shell exits (via `exit` or `Ctrl-D`, for example), your original shell
is resumed and your are put back into it.

```d2 scale="1.0"
shape: sequence_diagram
user_shell: User shell
subshell: Subshell

user_shell -> subshell: flox activate
subshell -> subshell: do work in the subshell
subshell -> user_shell: exit
```

### In-place

This method is similar to the first in that you're still in an interactive
shell,
but in this case it's the original shell.

To make this happen you could do one of these options in Bash:

Option 1

```{ .bash .copy }
source <(flox activate)
```

Option 2

```{ .bash .copy }
eval "$(flox activate)"
```

In both cases Flox emits a script that configures the shell,
and the shell executes that code to configure itself.

```d2 scale="1.0"
shape: sequence_diagram
user_shell: User shell
user_shell -> user_shell: source <(flox activate)
user_shell."Back to you"
```

In order to configure a `default` environment that's activated for every new
shell,
you would put a line like this in your `.bashrc`, `.zshrc`, `.tcshrc`, or
`config.fish`.
You could do this manually, but Flox will also prompt you to do it for you
the first time you attempt to install a package in a directory without an
environment and with no environments currently active.

### Shell Command

Sometimes you just want to run a command in the context of your environment,
maybe because you have some tools available in your environment that aren't
available outside the environment.

You could do this in a subshell:

- Enter the subshell via `flox activate`
- Run the command
- Exit the subshell via `exit`

You could do a similar thing with an in-place activation:

- Configure your existing shell with `source <(flox activate)`.
- Run the command
- Your shell is still configured by Flox when you're done

That's a lot of ceremony to run that one command though,
and the in-place activation leaves the environment still activated in your
shell,
which you may not want.

The easy way to do this is:

```{ .bash .copy }
flox activate -c "<your command>"
```

This starts a Flox-configured subshell, runs your command,
and immediately exits to put you back into your shell.

```d2 scale="1.0" pad="1"
shape: sequence_diagram
user_shell: User shell
subshell: Subshell
user_shell -> subshell: "flox activate -c cmd"
subshell -> subshell: run "cmd"
subshell -> user_shell: automatic exit
user_shell."Back to you"
```

### Exec Command

The final way to activate an environment is to exec a command directly without an intermediate shell, which can be done with:

```{ .bash .copy }
flox activate -- <your command>
```

This is similar to `activate -c` in that it activates the environment, runs a
command, and then exits.

Unlike `-c`, when exec'ing a command directly with `--`:

1. `[profile]` scripts aren't run
1. Shell syntax isn't supported, so it's not possible to chain commands (e.g. `cmd1 && cmd2`), use shell builtins, or use aliases.

When none of those features are needed, using `--` is faster than `-c` since
there's no intermediate shell.

## Activation flow

In order to understand where `hook` and `profile` fit into the picture,
we need to explore the timeline of what an activation looks like.
Much of this is dictated by what gets inherited when you create subshells.
Don't feel like you need to understand this entirely in order to use Flox,
it's just here to help you if you want a deeper understanding.

### What's inherited by a subshell?

When you create a subshell,
you create a new process that _happens_ to be a shell.
A new process inherits the environment of its parent process by default,
meaning that it inherits all of the environment variables set by that process.
If the parent process is a shell,
the functions and aliases defined in the parent process (shell) are not passed
down to the subshell (unless you use [special options like `export -f`][bash-func-export]).
This means that if we want you to be able to define functions and aliases to be
used by _your_ shell in your environment,
we have to make your shell source their definitions.

### Timeline

In order to meet our constraints and user experience goals,
we activate an environment in a number of steps.
The steps for a subshell activation are shown in the diagram below,
and they're very similar for the other types of activation.
Let's break it down step by step.

```d2 scale="1.0"
shape: sequence_diagram
user_shell: User shell
proc: New process

user_shell -> proc: call "flox activate"
flox activate: {
  proc -> proc: exec bash activation_script.sh
}
bash: {
  proc -> proc: run setup scripts
  proc -> proc: set user variables
  proc -> proc: source hook.on-activate
  proc -> proc: exec FLOX_SHELL
}
FLOX_SHELL: {
  proc -> proc: "source [profile] scripts"
  Do work: {
    proc -> proc: Do your work inside the shell
  }
}
proc -> user_shell: exit
```

For a variety of reasons it's convenient to have the same process ID (PID)
throughout the lifecycle of the activated environment.
The way you tell the current process to run a different program is via the
`exec` command (which calls the `exec` system call).

`flox activate` `exec`s a Bash subshell with a script that's bundled with Flox,
and sets some environment variables to be present in that Bash subshell.
We use this Bash subshell to prepare the way for putting you into a configured
instance of your shell of choice.
In the diagram above your shell of choice is represented with the `FLOX_SHELL`
variable,
which is also the variable you can use to override which shell Flox uses when
you activate an environment.

As part of this activation script,
Flox runs some initial setup, then sets the variables you've provided in the
[[vars] section of your manifest][vars-section].
Next, the script _sources_ the `hook.on-activate` script that you've provided
in the [[hook] section of your manifest][hook-section].
Since this script is run by the Bash shell we're using,
you only need to worry about the synax and oddities of one shell when writing
this script.
This is convenient, but it comes with some tradeoffs.

This Bash subshell is _non-interactive_.
Some programs behave differently when they execute in a shell that's not
interactive,
and most shells will not (by default) expand aliases when run non-interactively.
Also, remember that any functions or aliases you define in this Bash subshell
via the `hook.on-activate` script will not be inherited by your shell later.

Finally, we `exec` your shell with some overrides that allow us to inject our
own configuration,
such as `source`ing the scripts defined in the
[[profile] section of your manifest][profile-section].
Once those scripts have been sourced,
we hand control back to you.
Since the scripts in the `[profile]` section are sourced by your shell,
this is where you can define aliases and functions that you'd like to be
available in your activated environment.

### hook vs. profile in a nutshell

So, that was a lot of technical detail.
To make life easier for you when it comes to writing scripts for your
environment,
here is some simple guidance:

**hook.on-activate**:

- Always Bash, so there's only one shell syntax and set of quirks to keep in mind.
- Can't use aliases.
- Can define functions to use within the hook, but they won't be passed down to other shells.
- _Can_ define environment variables that need to be computed.

**profile**:

- Syntax depends on the shell.
- Can define functions and aliases.
- Can source scripts needed for other programs to work properly e.g. the `activate` script for a Python virtual environment.
- _Can_ define environment variables that need to be computed.

In short, it's probably best to put as much as you can in `hook.on-activate`
until you have shell-specific needs, you need aliases, or you need to source
a third-party script into your shell.

## Attaching

Everything we've discussed so far is about what happens when you start a new
activation of an environment.
However, if you're simply activating a second instance of an environment,
all of the setup done in your `hook` and script will already have
been done,
so you would be doing the same exact thing.
In addition, you would be setting all of the same exact environment variables
from your `[vars]` `[hook]` sections as before.

In short, this would be doing a lot of pointless work.
For that reason, we record those environment variables and apply them to
subsequent activations rather than computing them again.
We call this "attaching" to an activation, and we do it automatically for you
to make activation as fast as possible.

```d2 scale="1.0"
shape: sequence_diagram
shell1: First shell
shell2: Second shell
files: \"Somewhere\"

shell1 -> shell1: flox activate
shell1 -> files: save environment variables
shell1."Activated"
shell2 -> shell2: flox activate
shell2 <- files: restore environment variables
shell2."Activated"
```

If you edit your manifest and activate in a new shell,
the whole activation process is run again and subsequent activations will
attach to this new version of the environment.

## Development vs. runtime mode

See the [`options.activate.mode`](../man/manifest.toml.md#options) option in the manifest.

## Conclusion

As you can see, there's a lot going on under the hood,
but at the end of the day it's just Unix fundamentals:
processes and environment variables.

This is what makes activating a Flox environment so fast.
There's no container to build and there's no VM to boot up.
It really is a return to basics, with our own special twist on it.

Hopefully after reading this you have a deeper understanding of how a Flox
environment is activated,
and you feel confident that you can write `[hook]` and `[profile]` scripts
that prepare your environment just how you like them.

[environment-concept]: ./services.md
[bash-func-export]: https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html#index-export
[vars-section]: ../man/manifest.toml.md#vars
[hook-section]: ../man/manifest.toml.md#hook
[profile-section]: ../man/manifest.toml.md#profile

---


## What is the Base Catalog

> Source: `concepts/base-catalog.md`

---
title: What is the Base Catalog?
description: Everything you need to know about the Base Catalog
---

# What is the Base Catalog

The base Catalog is the root of all packages in Flox.
It is generated from a fork of [nixpkgs][nixpkgs],
contains historical metadata
(such as versions and system support over time),
and is updated on an automated schedule.
When you install something with Flox,
it will come from
or will be built upon the Base Catalog data.

On a regular basis,
Flox will evaluate a subset of packages
from its [nixpkgs][nixpkgs] fork
and save the metadata from the evaluation.
This makes it available to users of Flox.

An addional process continously checks newly added packages
and records actual build information (narino) from `nixos.cache.org`.
This along, with considerations for packages flagged as _unfree_ and _broken_,
allows flox to make attempts to serve up known good builds.
If you encounter a difference between `flox show` (meta data only),
and what `flox install` gives you, it may be due to this logic.
Refer to `allow_broken`, `allow_unfree`, and `allow_missing_builds`
in the [environment manifest][manifest_concept] to override the defaults.

## Which packages does Flox evaluate?

Generally, Flox evaluates `legacyPackages.<system>.*`
and follows the `recurseForDerivations` attribute.
In addition to this,
some explicit paths are evaluated.
The following is the current set,
but is likely to change over time.

For all system types:

- `nodePackages`
- `rustPlatform.rustLibSrc`
- `nodePackages_latest`

Additionally for `darwin` system types:

- `darwin`
- `swiftPackages`
- `swiftPackages.darwin`

## Update schedule

Evaluating all of nixpkgs on every commit
of the nixpkgs repository
is computationally expensive and often unnecessary.
Instead, Flox ingests the equivalent of the nixos-unstable branch
on a daily basis.
This means that once a package has landed on nixos-unstable
you can expect it in the Base Catalog within a day.

It's important to note
that this is distinct from the time between merging a pull request on the nixpkgs repository
and when that package becomes available in the Base Catalog.
The nixpkgs repository performs a series of checks after merging a pull request,
and changes are merged into a series of different branches
as different checks are performed on the attributes (packages) changed by the pull request.
This process can take anywhere from a couple of days to over a week
depending on whether the change causes breakage
in other packages in the nixpkgs repository.

If you have submitted a pull request to nixpkgs
and are interested in tracking its progress,
you can use this site: [Nixpkgs PR Tracker][nixpkgs_tracker].

### Flox branches

Flox maintains a fork of [nixpkgs][floxpkgs]
and maintains several branches.
These branches
relate to a Flox concept of "stabilities"
that is not yet fully exposed.
These are not to be confused with upstream branches of the same name,
and all derive from the `unstable` branch
of our [fork][floxpkgs]
(which, again, is not the same thing as `nixos-unstable`).

- `unstable` is reset to upstream `unstable` daily
- `staging` is reset to the `unstable` branch of our [fork][floxpkgs] each Saturday
- `stable` is reset to the `staging` branch of our [fork][floxpkgs] on the first Saturday of the month
- `lts` is reset to the `stable` branch of our [fork][floxpkgs] on the first Saturday in January and July (every 6 months)

These "stability" channels
will be exposed in the future,
allowing users to select a varying frequency of updates.
This architecture
also allows for patches
and backporting of fixes
against all stabilities.

Note that these branches do NOT reflect upstream branches of similar name,
or release channels.
Backporting that occurs on those branches
is not yet available via Flox.

### Delays

Since the Flox Base Catalog is based on upstream `nixos-unstable`,
it is subject to any delays
that occur during the regular operations of the Nix ecosystem.
If there is breakage
or if an update causes significant rebuilds,
it may be deferred to a longer process
and further delay its arrival on `nixos-unstable`,
and subsequently in the Flox Base Catalog.

### Retention

Storage is not boundless
so Flox uses the stabilities to garbage collect
package metadata when new packages are added.
When a stability is updated,
a tag is created in the form of `<stabilty>.<date>`.
The last `N` tags of each stability are retained.
This means revisions may "fall out" of the catalog over time.
Existing lockfiles save the metadata and will work forever.
However, a `flox update` to an environment
that contins a specific version,
_may_ in the future fail to resolve.
In practice, with our retention settings,
this is very unlikely.
Weekly captures are generally sufficient
to capture every package change,
in effect keeping every version in the past 3 years availble.

Current settings:

- `unstable` - 180 tags (6+ months daily)
- `staging` - 156 tags (3 years weekly)
- `stable` - 60 tags (5 years monthly)
- `lts` - 12 tags (6 years bi-annual)

[nixpkgs]: https://github.com/NixOS/nixpkgs
[floxpkgs]: https://github.com/flox/nixpkgs
[nixpkgs_tracker]: https://nixpkgs-tracker.ocfox.me
[manifest_concept]: ./environments.md#manifesttoml

---


## Building with Flox

> Source: `tutorials/build-and-publish.md`

---
title: Build and publish packages
description: Building and publishing custom packages with Flox
---

# Building with Flox

At some point during the development process you typically want to build your application so that it can be distributed or run.
Flox aims to be the one tool that you need for the entire software development lifecycle, so let's see how you can not only _develop_ your software with Flox, but _build_ it with Flox as well.

## Prepare a project

Let's start by creating a simple Go project.
We'll create a directory called `myproject` and create a Flox environment inside of it so we can install our tools.

```text
$ mkdir myproject
$ cd myproject
$ flox init
✨ Created environment 'myproject' (aarch64-darwin)

Next:
  $ flox search <package>    <- Search for a package
  $ flox install <package>   <- Install a package into an environment
  $ flox activate            <- Enter the environment
  $ flox edit                <- Add environment variables and shell hooks
```

Since we're using Go, we'll want to install Go:

```text
$ flox install go
✅ 'go' installed to environment 'myproject'
$ # let's see what version of Go we have
$ flox list
go: go (1.24.1)
```

Now let's add some very minimal code so that we have something to build.
For now this will be a very simple "hello world" application.
Start by activating the environment so that we have our Go application available.

```text
$ flox activate
✅ You are now using the environment 'myproject'.
To stop using this environment, type 'exit'

flox [myproject] $ go mod init hello
go: creating new go.mod: module hello
flox [myproject] $ touch main.go
```

Now edit `main.go` to have the following contents:

```go
package main

import "fmt"

func main() {
  fmt.Println("Hello World")
}
```

Now let's ensure that we can build the `hello` program:

```text
flox [myproject] $ go build
flox [myproject] $ # ensure that 'hello' was built
flox [myproject] $ ls -al
.rw-r--r--   24 zmitchell 27 Mar 14:31 go.mod
.rwxr-xr-x 2.4M zmitchell 27 Mar 14:32 hello
.rw-r--r--   77 zmitchell 27 Mar 14:32 main.go
```

We can build the program, so let's verify that we can run it:

```text
flox [myproject] $ # ensure that 'hello' runs
flox [myproject] $ ./hello
Hello World
```

Everything appears to be in working order, so now we can discuss what it looks like to build the program with Flox instead of running the build commands ourselves.

## Define a build

In order to define a Flox build, we add an entry to the [`[build]`][flox-manifest-build-section] section of the manifest.
Every name added to the `build` section creates a new package.
In our case the package will be the compiled Go program, but you can use Flox to build all kinds of things.
See the [builds][build-concept] page for more examples of what you can build with Flox.

All that's necessary to define a build is a short script that does two things:

- Runs any commands necessary to build the program
- Copies the program to a directory called `$out`

The `$out` shell variable holds the path to a temporary directory where your build package should be placed (again, "package" in our case means the compiled `hello` program).
The `$out` directory adheres to the [Filesystem Hierarchy Standard (FHS)][fhs], which is just the formal name for the convention of placing executable files in `/bin`, libraries in `/lib`, etc.
For this `hello` program we'll want to place it in `$out/bin` since `hello` is an executable program, and that's where the FHS says to put those types of files.
Flox expects you to put executables there, and if you put them somewhere else you may experience unexpected behavior.

Let's now define our build.
Run [`flox edit`][flox-edit] so that you can edit your manifest, and add the following section:

```toml
[build.hello]
description = "My custom program printing hello world in Go"
command = '''
  mkdir -p $out/bin
  go build # produces the ./hello executable file
  cp hello $out/bin/hello
'''
```

## Perform a build

It's the moment of truth, let's run [`flox build`][flox-build] to have Flox build our `hello` program for us:

```text
flox [myproject] $ flox build
Rendering hello build script to /var/folders/qn/77rf0syj2s7djp588bzp5vkm0000gn/T//d6f2efa3-hello-build.bash
Building hello-0.0.0 in local mode
00:00:00.004571 + go build
00:00:00.205192 + mkdir -p /tmp/store_d6f2efa321a606aebf3b41d0d96ace1d-hello-0.0.0/bin
00:00:00.207584 + cp hello /tmp/store_d6f2efa321a606aebf3b41d0d96ace1d-hello-0.0.0/bin/hello
this derivation will be built:
  /nix/store/g3z03h4p2xa9rf6y78d0xamryggawvha-hello-0.0.0.drv
building '/nix/store/g3z03h4p2xa9rf6y78d0xamryggawvha-hello-0.0.0.drv'...
hello-0.0.0> patching script interpreter paths in /nix/store/2hc9mjxs6wqcd8cscw9ll650jv1k6wn1-hello-0.0.0/bin/hello
Completed build of hello-0.0.0 in local mode

✨ Build completed successfully. Output created: ./result-hello
```

It worked!
The last line of output tells us that the built output was created in our current directory and called `result-hello`.
Every build output has the name `result-<name>` where `<name>` is the name you used in the `[build]` section of your manifest (for example `[build.hello]`).

This `result-hello` file is actually a symbolic link to the final destination of the `$out` directory.
That means we can't run `result-hello` directly, and instead we need to run `result-hello/bin/hello`.
Let's do that now:

```text
flox [myproject] $ ./result-hello/bin/hello
Hello World
```

## Define a second build

It's possible to define more than one build for your Flox environment.
Why would you want to do that?
In our case we have a Go program, and by default the Go compiler optimizes for fast builds, but not necessarily fast or small executables.
This makes development nice because you get the fastest possible feedback cycle when developing your software, but in production you probably want a more optimized program.
We can define one build for development, and another build for our "production" `hello` program, both using the same source code and tools!

Run `flox edit` to edit your manifest again, and add this new build:

```toml
[build.hello-opt]
command = '''
  go build -ldflags="-s -w" -gcflags="-l=4"
  mkdir -p $out/bin
  cp hello $out/bin/hello
'''
description = "A program that greets you, very quickly"
version = "1.0.0"
```

This build produces a version of our `hello` program with some optimizations applied.
Now if you run `flox build` it will run both the `hello` and `hello-opt` builds, or we could specify just the `hello-opt` build with `flox build hello-opt`:

```text
flox [myproject] $ flox build hello-opt
Rendering hello-opt build script to /var/folders/qn/77rf0syj2s7djp588bzp5vkm0000gn/T//60dfcc45-hello-opt-build.bash
Building hello-opt-1.0.0 in local mode
00:00:00.004522 + go build '-ldflags=-s -w' -gcflags=-l=4
00:00:00.155021 + mkdir -p /tmp/store_60dfcc45203ccd97815dbc9aecc6d84d-hello-opt-1.0.0/bin
00:00:00.157435 + cp hello /tmp/store_60dfcc45203ccd97815dbc9aecc6d84d-hello-opt-1.0.0/bin/hello
this derivation will be built:
  /nix/store/k6za2nx7jla6rwzs7lj1qm4rc03v9z7q-hello-opt-1.0.0.drv
building '/nix/store/k6za2nx7jla6rwzs7lj1qm4rc03v9z7q-hello-opt-1.0.0.drv'...
hello-opt-1.0.0> signing /nix/store/nbykbq9fy0z67hhlf1kvf8wk7wb29x59-hello-opt-1.0.0
hello-opt-1.0.0> patching script interpreter paths in /nix/store/nbykbq9fy0z67hhlf1kvf8wk7wb29x59-hello-opt-1.0.0/bin/hello
Completed build of hello-opt-1.0.0 in local mode

✨ Build completed successfully. Output created: ./result-hello-opt
```

## Publish the package

--8<-- "paid-feature.md"

Now that the package is built, we can send it somewhere.
Every user has a private catalog that they can publish packages to.
In order to share packages with other people you must create an organization.
This is a paid feature, and if you would like access to it you should contact Flox directly.
See the [organizations][organizations-concept] page for more details.

Now that you've built the package you can [publish][publish-concept] it to your private catalog via the [`flox publish`][flox-publish] command.
This command has a few requirements to make sure that the package you're publishing can be built by other people reproducibly:

- The Flox environment must be in a git repository.
- All tracked files in the repository must be clean.
- The repository must have a remote configured.
- The current revision must be pushed to the remote.
- The Flox environment must contain at least one package so that the published package can be attached to a point in time in the Base Catalog (where our `go` package came from).

Let's say that we've done all of that so that we can publish our `hello` program:

```text
flox [myproject] $ flox publish hello
```

The `flox publish` command performs a clean build of the package in a temporary directory to ensure that the build doesn't depend on anything outside of the git repository.

## Install the package

--8<-- "paid-feature.md"

Now that you've published the package, it will show up in [`flox search`][flox-search] and [`flox show`][flox-show], and can be installed via [`flox install`][flox-install].
The package will appear with your username or organization name prefixed to the package name.
Let's say your username is `myuser` and the package name is `hello`, in which case the published package will appear as `myuser/hello` in `flox show`, `flox search`, and `flox install`.
Let's see that in action with `flox search`:

```text
flox [myproject] $ flox search hello
myuser/hello                My custom program printing hello world in Go
hello                       Program that produces a familiar, friendly greeting
hello-go                    Simple program printing hello world in Go
hello-cpp                   Basic sanity check that C++ and cmake infrastructure are working
nwg-hello                   GTK3-based greeter for the greetd daemon, written in python
hello-unfree                Example package with unfree license (for testing)
hello-wayland               Hello world Wayland client
sbclPackages.hello-clog     <no description provided>
texlivePackages.othello     Modification of a Go package to create othello boards
sbclPackages.hello-builder  <no description provided>

Showing 10 of 23 results. Use `flox search hello --all` to see the full list.

Use 'flox show <package>' to see available versions
```

You can see that our `myuser/hello` package is the first result.
Now that we know it's available, let's install it:

```text
flox [myproject] $ flox install myuser/hello
✅ 'myuser/hello' installed to environment 'myproject'
```

## Conclusion

With Flox you have an integrated experience where the same tool you use to develop software is also used to build it, publish it, and eventually consume it.
The story doesn't end here though.
In this guide we've shown you how to build and distribute programs, but you can also use it to distribute configuration files (or any other file).
See the [builds][extra-builds] concept page for examples of what else you can build and publish with Flox.

[flox-manifest-build-section]: ../man/manifest.toml.md#build
[build-concept]: ../concepts/builds.md
[fhs]: https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
[flox-install]: ../man/flox-install.md
[flox-show]: ../man/flox-show.md
[flox-search]: ../man/flox-search.md
[flox-edit]: ../man/flox-edit.md
[flox-build]: ../man/flox-build.md
[flox-publish]: ../man/flox-publish.md
[extra-builds]: ../concepts/manifest-builds.md#example-configuration-files
[publish-concept]: ../concepts/publishing.md
[organizations-concept]: ../concepts/organizations.md
[early]: https://flox.dev/early/

---


## Builds

> Source: `concepts/builds.md`

---
title: "Builds"
description: Understanding how to build packages with Flox
---

The typical development lifecycle involves a step where your source code and potentially some other assets are bundled together into a package.
That package could be a compiled executable, an archive containing source files, or something else entirely.

A Flox environment ensures that the same set of tools, dependencies, and environment variables are available where the environment is activated, whether that's during development, running in CI, or _when building packages_.
Flox environments have native support for defining builds that should be performed in the context of the environment, making it quick and easy to transition from _developing_ your software in a reliable and reproducible way, to _building_ your software in a reliable and reproducible way.

## Defining builds

There are two ways to define builds, depending on your needs:

* [Manifest builds][manifest-builds-concept] allow you to use the tools and commands you're already familiar with to easily build packages with a reasonable amount of reproducibility
* [Nix expression builds][nix-expression-builds-concept] are for truly reproducible builds and modify existing packages, if you're already familiar with or willing to learn some of the Nix language

## Performing builds

Builds are performed with the [`flox build`][flox-build] command.
When invoked with no other arguments, `flox build` will execute each build defined in the environment.
You can optionally specify which builds to perform:

```{ .bash .copy }
flox build myproject
```

For each build that `flox` successfully executes, a symlink named `result-<name>` will be placed in the root directory of the project.
These symlinks link to the read-only locations where the contents of each package are stored.
Continuing with the `myproject` example, after the build you could run the compiled binary via

```{ .bash .copy }
./result-myproject/bin/myproject
```

## Cross-platform builds

When you build a package, it is built on your host machine, and therefore only built for the system (`aarch64-darwin`, `x86_64-linux`, etc) of your host machine.
This means that if you want packages built for multiple platforms, you need to run the build on multiple platforms.
One way to accomplish this is to run your builds in [CI][flox-ci-cd].

[manifest-builds-concept]: ./manifest-builds.md
[nix-expression-builds-concept]: ./nix-expression-builds.md
[flox-build]: ../man/flox-build.md
[flox-ci-cd]: ../tutorials/ci-cd.md

---


## C/C++

> Source: `languages/c.md`

---
title: C/C++
description: Common questions and solutions for using C with Flox
---

# C/C++

## Build with Flox

Not only can you _develop_ your software with Flox, but you can _build_ it as well.
See the [builds][build-concept] concept page for more details.

### Manifest builds

#### Autotools

Since `autotools` isn't specific to C, this example will also work for any project using `autotools`.
Since the output of the build must be copied to the `$out` directory, you must set the install prefix to `$out`.

```toml
[build.myproject]
command = '''
  ./configure --prefix=$out
  make
  make install
'''
```

#### CMake

Doing a `CMake` build looks much the same as `autotools`.

```toml
[build.myproject]
command = '''
  cmake -DCMAKE_INSTALL_PREFIX=$out
  make
  make install PREFIX=$out
'''
```

### Nix expression builds

To build a project using `clang`:

```nix
{ clangStdenv }:

clangStdenv.mkDerivation {
  pname = "myproject";
  version = "0.0.1";
  src = ../../.;

  installFlags = [ "PREFIX=$(out)" ];
}
```

[build-concept]: ../concepts/builds.md

---


## Setting up a Catalog Store

> Source: `customer/catalog-store.md`

---
title: Catalog Store
description: Create a Catalog Store for publishing your own Flox packages
---

# Setting up a Catalog Store

Note that this page is only relevant if your organization has chosen to provide its own Catalog Store.
By default provides a pre-configured Catalog Store to each organization as part of the organization's private Catalog.

A user-provided Catalog Store is an AWS S3 bucket
or any S3 compatible service, like [MinIO][minio-s3-compatible]{:target="\_blank"}
or [Backblaze B2][backblaze-b2-cloud-storage]{:target="\_blank"}. (For the
sake of simplicity, this guide focuses on S3, but there are other providers
available if you prefer them to AWS.)

To configure your Catalog to use this Catalog Store, you will need to set ingress (where new packages are uploaded to) and egress (where packages are downloaded from) URIs for the Catalog.
This is done with a command line utility provided by Flox.

[minio-s3-compatible]: https://min.io/product/s3-compatibility
[backblaze-b2-cloud-storage]: https://www.backblaze.com/cloud-storage

## Configure an AWS S3 bucket

The first step in setting up your Catalog Store is creation and configuration of
an AWS S3 Bucket. There are numerous ways to accomplish this, including the AWS
Console, the AWS CLI, and Terraform (or another infrastructure-as-code tool),
to name a few. These processes are well documented, but to get started,
it's best to refer directly to AWS documentation.

- [What is Amazon S3?][amazon-s3]{:target="\_blank"}
- [AWS S3 CLI Reference][aws-cli-reference-s3]{:target="\_blank"}
- [Amazon Simple Storage Service API Reference][aws-s3-api-reference]{:target="\_blank"}

Once your S3 bucket is set up and configured with the access policies deemed
necessary by your organization's internal policies, you're ready to proceed to
the next step. Someone from Flox can help you if you run into trouble during
the setup process. Simply reach out to your designated point of contact,
and we'll work with you to get you up and running.

[amazon-s3]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
[aws-cli-reference-s3]: https://docs.aws.amazon.com/cli/latest/reference/s3/
[aws-s3-api-reference]: https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html

### Policy example

By default, S3 buckets are normally confined to be read by the bucket owner or users within the same AWS account. This is likely a decent starting point for the Catalog Store. However, if you'd like to make your published Flox software available to a wider audience, you can use the following policy as a starting point. Note this will make the contents of the bucket public, so be sure to understand the implications of this before applying it.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowPublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::$BUCKET_NAME/*"
    }
  ]
}
```

## Ensure the Nix Daemon has access to the S3 Bucket

As you probably know by now, the underlying technology powering Flox is Nix.
Accordingly, we need to take a couple steps to ensure that the Nix daemon
has access to the S3 bucket you've just created.
To do so, we need to get AWS credentials, specifically `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and, if applicable, `AWS_SESSION_TOKEN`.
Use the `aws configure` or `aws configure sso` command [as described in the CLI reference][aws-cli-configure-command]{:target="\_blank"} to set those same values, and ensure that the AWS profile and region match those configured for the S3 bucket.

You can confirm that everything is set up correctly by inspecting the values stored in `$HOME/.aws/credentials`.

[aws-cli-configure-command]: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/index.html#configure

## Set Catalog Store ingress and egress URIs

Reach out to your Flox point of contact to accomplish this step.

## Create and set a signing key

At this point, you should have an appropriately configured Catalog Store
to which you can publish your own software via the `flox publish` command.
In order for users to upload artifacts to the Catalog Store and then install those artifacts, you must configure public and private signing keys.

The private key is used to sign artifacts before uploading them, whereas the public key must be distributed to anyone you wish to be able to install those published artifacts.
See the [signing keys][signing-keys] Cookbook page for instructions on configuring your signing keys.

[signing-keys]: ./signing-keys.md

---


## Continuous integration/delivery (CI/CD)

> Source: `tutorials/ci-cd.md`

---
title: Running Flox in CI/CD
description: Integrate with your favorite CI/CD platform.
---

# Continuous integration/delivery (CI/CD)

Continuous integration (CI) and Continuous delivery (CD) is essential in today's software development cycle.
With Flox the **exact** same set of software can be used for local development and a CI/CD pipeline.
This feature works out of the box with Flox because Flox environments work cross-platform and reproducibly by default.
This means that you can spend less time debugging your CI/CD pipeline and more time developing your software.

Let's look at how you can use Flox with a variety of CI/CD platforms.
For the following examples assume that you have a repository that contains a Flox environment, and assume that you've installed some Node.js dependencies for your project.

## Github Actions

Flox provides two different actions that you can use in a GitHub Actions workflow:

- `flox/install-flox-action`: This action installs the Flox CLI so you can run Flox commands as you would locally. At some point you would typically run `flox activate -c "<your command>"` with this action to run a command inside the Flox environment.
- `flox/activate-action`: This action allows you to skip activating the environment yourself and simply provide the command that you would like to run in the environment.

Note that the `flox/install-flox-action` is still required if you want to use `flox/activate-action`.

Here is an example workflow that installs the Flox CLI, runs `npm run build`
inside the project's environment, and runs `netlify deploy` inside a FloxHub
environment:

```yaml title=".github/workflows/ci.yml"
name: "CI"

... # (1)!

jobs:

  build:
    name: "Build website"
    runs-on: "ubuntu-latest"
    steps:
      - name: "Checkout"
        uses: "actions/checkout@v4"

      - name: "Install Flox" # (2)!
        uses: "flox/install-flox-action@v2"

      - name: "Build" # (3)!
        uses: "flox/activate-action@v1"
        with:
          command: npm run build

    - name: Activate remote environment
      uses: flox/activate-action@v1
      with:
        environment: my-username/my-netlify-env
        command: netlify deploy
```

1. You are looking at an example project, your project will probably look a little different. Important parts of how to integrate Flox with Github Actions are highlighted below.
2. `flox/install-flox-action` will install the latest version of Flox.
3. `flox/activate-action` allows you to run a command inside the Flox environment.

## CircleCI

There is a [Flox Orb](https://github.com/flox/flox-orb) that helps you use Flox inside CircleCI.
Similar to GitHub Actions there is a `flox/install` step and a separate `flox/activate` step.

Here is an example CircleCI workflow that installs Flox and runs `npm run build` inside the environment:

```yaml title=".circleci/config.yml"
version: 2.1

orbs:
  flox: flox/orb@1.0.0

jobs:
  build:
    machine:
      image: ubuntu-2204:current
    steps:
      - checkout
      - flox/install # (1)!
      - flox/activate: # (2)!
          command: "npm run build"
```

1. The `install` command will install the latest Flox version. You can change the `channel` and `version` options which allow you to select exactly which version of Flox to install. The `channel` option will install the latest version from the specified channel, and the `version` option will install a specific version.
2. The `activate` command runs a command in the context of a Flox environment.

## GitLab

To run Flox in a GitLab pipeline you use a container image with Flox preinstalled.
Flox provides the `ghcr.io/flox/flox` image for you to use in your pipelines.
Inside the container you have access to the full Flox CLI, so running a command in the container looks the same as it would locally: `flox activate -c "<your command>"`.

Here is an example GitLab pipeline that uses a Flox container to run `npm run build` inside the environment:

```yaml title=".gitlab-ci.yml"
build:
  stage: build
  image: ghcr.io/flox/flox:latest # (1)!
  script:
    - flox activate -c "npm run build" # (2)!
```

1. Use the `ghcr.io/flox/flox` container image, which comes with Flox already installed.
2. Run a command in the Flox environment.

## Suggestions

Now that you know _how_ to use your Flox environment in CI/CD, the world is your oyster.
Here are some suggestions for things you can do with your Flox environment in CI:

- Run a linter to ensure that new changes adhere to your team's style.
- Use [flox containerize][containerize] to build a container from your environment to deploy elsewhere.
- Build artifacts for multiple systems.
- Run a link checker over your documentation.

## Where to next?

- :simple-readme:{ .flox-purple .flox-heart } [Sharing environments][sharing_guide]

- :simple-readme:{ .flox-purple .flox-heart } [Layering multiple environments][layering_guide]

- :simple-readme:{ .flox-purple .flox-heart } [Customizing the shell hook][customizing_guide]

[sharing_guide]: ./sharing-environments.md
[layering_guide]: ./layering-multiple-environments.md
[customizing_guide]: ./customizing-environments.md
[containerize]: ../man/flox-containerize.md

---


## Composing environments

> Source: `concepts/composition.md`

---
title: Composing environments
description: How to combine and reuse environments.
---

# Composing environments

When your company starts work on a new service, it's likely that the tools required to work on this service will be very similar to the tools used to work on other services at the company.
Similarly, when you work on hobby projects it's likely that you use a similar set of tools from one project to the next.
With other developer environment solutions it's common to need to recreate your developer environment from scratch for each new project.

With Flox you can define a toolchain or service once and _compose_ it with others to create a composed environment.
Put another way, **with Flox you can create developer environments from reusable building blocks**.
Reuse and composition are two features that have long been a Holy Grail for developer environments, and Flox makes these features friendly and easily accessible.

## Building blocks

Environments are the building blocks from which a "composed" environment is created.
In this composition there is a hierarchy consisting of a "composing" environment and a list of "included" environments that it treats as dependencies.
The manifests of the included and composing environments are merged and then the resulting "merged" manifest is locked and built.

```d2 scale="0.9"
composer: "Composing\nenvironment"

includes: Included environments {
  envA: Env A
  envB: Env B
  envC: Env C
  direction: down
  envA -> envB: Overridden by
  envB -> envC: Overridden by
}

includes -> composer: Overridden by
```

## Including an environment

The included environments are declared in your manifest in the `include` table under the `environments` array.
Each entry in this array is an "include descriptor", which specifies where to find the environment.

```text
IncludedEnvironments ::= [IncludeDescriptor]
IncludeDescriptor ::= LocalIncludeDescriptor | RemoteIncludeDescriptor
LocalIncludeDescriptor :: = {
  dir  = STRING
, name = null | STRING
}
RemoteIncludeDescriptor :: = {
  remote = STRING
, name   = null | STRING
}
```

Just like you would use the `flox activate --dir` flag to specify an environment to activate by its path, you use the `dir` field to specify the path to an environment to include.
Every environment has a name built-in, but sometimes there may be name conflicts, or you may just want to provide a different name.
You can do so with the `name` field.

An example `include` section is shown below:

```toml
[include]
environments = [
  # Include a local environment
  { dir = "../myenv" },
  # Override the name of an environment
  { dir = "../other_env", name = "other" },
  # Include a FloxHub environment
  { remote = "myuser/myenv" },
]
```

The order in which the included environments are listed matters.
The environments specified later in the list will override those earlier in the list.

It is possible to push a composed environment to FloxHub, but not if it includes environments that exist locally e.g. environments that are specified with the `dir` field.

## Merging process

When environments are composed, their manifests are merged into a single merged manifest.
The manifests are merged, and the merged manifest is locked (as opposed to building the environments and merging their lockfiles).
This allows manifests to override each other e.g. to ask for a newer version of a package specified in an earlier manifest in the merge process.

Later manifests override earlier manifests when there are conflicts, and the manifest of the composing environment always has the highest priority (it is applied last).
The `include.environments` array is stripped from included environments and the composing environment's manifest during the merge process.

The manifests are merged during the process of building the environment, and if one manifest overrides another, a warning is displayed.

Most manifest fields are merged the way you would expect:

`install`

:  The install section contains the union of all package descriptors from all manifests. When there are conflicts, the entire package descriptor is overridden.

`services`

: Same behavior as the `install` section.

`vars`

: Same behavior as the `install` section.

`hook.on-activate`

: The `hook.on-activate` scripts are appended to each other.

`profile`

: The corresponding scripts in the `profile` section are also appended to each other e.g. all of the `profile.common` scripts are appended, all of the `profile.bash` scripts are appended, etc.

`containerize`

: The options in the `containerize` section are more complicated because merging some options instead of overriding them would lead to unintuitive behavior.
`user`, `cmd`, `working-dir`, and `stop-signal` are completely overridden.
`exposed-ports`, `volumes`, and `labels` are merged.

`options`

: The options in the `options` section are all overridden completely.
This prevents a merge of `options.systems` from providing more systems than the environment can support.
Similarly, this prevents a merge of `allow.licenses` from allowing more licenses than intended.

One option to note is `options.activate.mode`.
Recall that the activation mode determines whether development dependencies of packages are added to `PATH`, etc when the environment is activated.
Since the default is `dev` mode, and the default doesn't appear in the manifest, a single environment that sets `options.activate.mode = "run"` will cause the merged manifest to also set this option.
This can be surprising, so check the manifests of the included environments and override this option if you're observing this behavior.

## Getting the latest manifests

It's reasonable to assume that the manifests of the included environments will change over time and at some point you will want to bring in the latest versions of those manifests.
This is accomplished with the `flox include upgrade` command.

Running this command will check each of the included environments and determine if there were changes to their manifests.
If the changes to the manifest have been built by the included environment, then the new manifest will be included.
At this point the merge process runs again, a new merged manifest is produced, and the composed environment is rebuilt from the new merged manifest.

---


## Reusing and combining developer environments

> Source: `tutorials/composition.md`

---
title: Reusing and combining developer environments
description: How to build developer environments out of reusable building blocks.
---

# Reusing and combining developer environments

It's common to use a very similar set of tools from one project to the next, but it's also very common to need to set up a developer environment from scratch from one project to the next.
In this tutorial you'll see how to significantly cut down on the work required to bootstrap new projects.

## Create a reusable toolchain

Let's say that you frequently work on Python projects and use [Poetry][poetry] as your package manager of choice.
If you work on a bunch of projects that need these tools, you can save yourself some time by creating an environment that contains `python312` and `poetry` and reusing it in some way.
Let's do that now and we'll show you some examples of different ways you can reuse it.

Create a new directory called `myproject` and `cd` into it.
Then create a new environment called `python_env` in it with the [`flox init`][flox-init] command.

```console
$ mkdir myproject && cd myproject
$ flox init -d python_env
✨ Created environment 'python_env' (aarch64-darwin)

Next:
  $ flox search <package>    <- Search for a package
  $ flox install <package>   <- Install a package into an environment
  $ flox activate            <- Enter the environment
  $ flox edit                <- Add environment variables and shell hooks
```

Your directory structure should now look like this:

```text
myproject/
  python_env/
    .flox
```

Now install `python312` and `poetry` to this environment with the [`flox install`][flox-install] command:

```console
$ flox install -d python_env python312 poetry
✅ 'python312', 'poetry' installed to environment 'python_env'
```

Now you can push this environment to [FloxHub][floxhub].
Once the environment is on FloxHub you can share it with other people, but, more importantly, you can now use it as a template for new projects.
Let's start by pushing the environment to FloxHub:

```console
$ flox push -d python_env
✅ python_env successfully pushed to FloxHub

Use 'flox pull myuser/python_env' to get this environment in any other location.

This environment is public.
You can view and edit the environment at https://hub.flox.dev/myuser/python_env
```

You may need to authenticate with FloxHub as part of running this command.
Instead of `myuser` you will see your username.

## Template environments

### Creating a template for new projects

Now that the environment is on FloxHub, we can use it to bootstrap new projects.
One way to do this is to make a new, local copy of the environment that's not connected to FloxHub.
You accomplish this with the [`flox pull --copy`][flox-pull] command.
Let's create a new copy of this environment in a directory called `new_python_project`:

```console
$ flox pull -d new_python_project --copy myuser/python_env
✨ Created path environment from myuser/python_env.

You can activate this environment with 'flox activate'
```

Your directory structure should now look like this:

```text
myproject/
  python_env/
    .flox/
  new_python_project/
    .flox/
```

At this point your `new_python_project` directory contains a Flox environment that already contains Python development tools, and you're ready to start developing.

### Staying in sync with the template

By using the `--copy` flag to `flox pull` we have created a new copy of the environment that is completely disconnected from the copy on FloxHub.
This makes sense if you plan to add project-specific dependencies, otherwise your template environment would accumulate dependencies not needed by _all_ of your Python projects.
The downside is that if someone makes changes to the template environment, your local copy won't get those updates.

In some cases, however, you may actually want your project to stay in sync with the template.
If that's something you want, you can simply omit the `--copy` flag and periodically run the `flox pull` command to get the latest updates to the environment.
This amounts to using the template environment directly.

## Composing environments

### Creating a composed environment

In the previous example we showed you how you could create a local copy of a template environment (and lose access to updates), _or_ use the template environment directly (and either stuff it full of every project's dependencies, or not add dependencies to it at all).
What if I told you that you could have the best of both worlds?
We call this feature "composition".

One environment (we call it the "composing" environment) can "include" another environment (we call this an "included" environment), treating it like a dependency.
You can install packages to the composing environment just like you would any other environment, which allows you to reuse the template environment, get updates to it, and add project specific dependencies directly to the composing environment.

Let's see an example of this in action.
As a reminder, you currently have this directory structure:

```text
myproject/
  python_env/
    .flox/
  new_python_project/
    .flox/
```

Let's create a environment in a `composed_python_project` directory.

```console
$ flox init -d composed_python_project
✨ Created environment 'composed_python_project' (aarch64-darwin)

Next:
  $ flox search <package>    <- Search for a package
  $ flox install <package>   <- Install a package into an environment
  $ flox activate            <- Enter the environment
  $ flox edit                <- Add environment variables and shell hooks
```

Your directory structure should now look like this:

```text
myproject/
  python_env/
    .flox/
  new_python_project/
    .flox/
  composed_python_project/
    .flox/
```

Pretend that this is the environment you would use to do your work on your Python project.
You're going to need a Python toolchain, and you may need some additional dependencies.
In order to bring in the Python toolchain we'll need to edit the manifest of the `composed_python_project` environment and include the `python_env` environment.
Run the [`flox edit`][flox-edit] command and make the `include` section of the manifest look like this:

```toml
[include]
environments = [
  { dir = "../python_env" }
]
```

This `include.environments` list tells the Flox CLI where to find the environments you'd like to include.
When there is more than one environment in this list, the order of the environments in the list also specifies their priority (later ones in the list have higher priority).
Once you save and exit you should see this output:

```console
✅ Environment successfully updated.
ℹ The following manifest fields were overridden during merging:
- This environment set:
  - options.systems
ℹ Run 'flox list -c' to see merged manifest.
```

As part of building the composed environment, the manifests of the included environments and the composing environment are merged, which means that some environments may install the same package, set the same environment variable, etc.
In those cases, the priority order of the environments determines which one wins, with the composing environment always having the highest priority.
When one manifest overrides another, you are shown a message indicating which fields were overridden so that there are no surprises.
The message about `options.systems` is simply a result of the fact that the default manifest sets this field explicitly.

If you now run [`flox list`][flox-list], you should see the packages from the `python_env` environment, even though we never ran a `flox install` command on the `composed_python_project` environment!

```console
$ flox list -d composed_python_project
poetry: poetry (2.1.1)
python312: python312 (python3-3.12.9)
```

Remembering that as part of the build process we merge manifests, if you want to see the final merged manifest you can use the `flox list -c` command.
When you use this command _without_ a composed environment, it prints the (unmerged) manifest.
When you use this command _with_ a composed environment, it prints the merged manifest.

```console
$ flox list -c -d composed_python_project
version = 1

[install]
poetry.pkg-path = "poetry"
python312.pkg-path = "python312"

[options]
systems = ["aarch64-darwin", "aarch64-linux", "x86_64-darwin", "x86_64-linux"]

ℹ Displaying merged manifest.
ℹ The following manifest fields were overridden during merging:
- This environment set:
  - options.systems
```

Notice that the `[install]` section contains the `python312` and `poetry` packages that were merged in from the `python_env` environment.

### Installing project specific dependencies

Now let's install some project-specific dependencies.
When you run the `flox install` command on a composing environment, the packages are installed to the composing environment itself, not the merged manifest or any of the included environments.
In short, it does what you would expect.

Let's add the `pytest` package:

```console
$ flox install -d composed_python_project python312Packages.pytest
✅ 'pytest' installed to environment 'composed_python_project'
```

Note that the message says the package was installed to the `composed_python_project` environment.
If you run `flox edit -d composed_python_project` you'll see that the package is contained in the `[install]` section of `composed_python_project`'s manifest.

### Getting the latest versions of included environments

At some point a template environment may change.
Say that you decide you want to use [hypothesis][hypothesis] for testing all of your Python projects.
To do that, you would install the `hypothesis` package to your `python_env` environment, and somehow propagate those changes to the composed environment.
This is accomplished with the `flox include upgrade` command, which fetches the latest versions of each of the included environments.

Let's add that package to `python_env`:

```console
$ flox install -d python_env python312Packages.hypothesis
✅ 'hypothesis' installed to environment 'myuser/python_env'
```

Now let's propagate those changes to the composed environment:

```console
$ flox include upgrade -d composed_python_project
✅ Upgraded 'composed_python_project' with latest changes to:
- 'python_env'
```

Now if you run `flox list` you should see that the composed environment now contains the `hypothesis` package:

```console
$ flox list -d composed_python_project
hypothesis: python312Packages.hypothesis (6.127.4)
poetry: poetry (2.1.1)
pytest: python312Packages.pytest (8.3.5)
python312: python312 (python3-3.12.9)
```

Remember, the only package that's installed to `composed_python_project` directly is `pytest`.
All of the other packages you get for free just by including the `python_env` environment.

### Including FloxHub environments

Environments can also be included directly from FloxHub, such as the `myuser/python_env` environment that we pushed previously.
This is especially useful if you're including the same environment across multiple projects and repositories because you don't need to ensure that they are checked out and synced locally.

Push the additional package that we installed to `myuser/python_env` earlier:

```console
$ flox push -d python_env
✅ Updates to python_env successfully pushed to FloxHub

Use 'flox pull myuser/python_env to get this environment in any other location.
```

Run the [`flox edit`][flox-edit] command and make the `include` section of the manifest look like this:

```toml
[include]
environments = [
  { remote = "myuser/python_env" }
]
```

After saving and exiting, the environment will now behave as it did with the local include:

```console
$ flox list -d composed_python_project
hypothesis: python312Packages.hypothesis (6.127.4)
poetry: poetry (2.1.1)
pytest: python312Packages.pytest (8.3.5)
python312: python312 (python3-3.12.9)
```

## Conclusion

The ability to reuse and combine environments means that you can now assemble a developer environment for a project from reusable building blocks.
This means you can spend less time getting started, and more time developing your software.
Similarly, since you're treating environments like dependencies, if you make an improvement to a template environment while working on one project, the improvement will become available to all of your other projects that use that environment as soon as they run `flox include upgrade`.

[poetry]: https://python-poetry.org/
[flox-init]: ../man/flox-init.md
[flox-pull]: ../man/flox-pull.md
[flox-install]: ../man/flox-install.md
[flox-edit]: ../man/flox-edit.md
[flox-list]: ../man/flox-list.md
[floxhub]: ../concepts/floxhub.md
[hypothesis]: https://hypothesis.readthedocs.io/en/latest/

---


## Configuration

> Source: `k8s/config.md`

---
title: "Configuration"
description: "Configuring Imageless Kubernetes"
---

# Configuration

## Authentication

Imageless Kubernetes allows you to run Flox environments in place of or on top of container images.
Flox environments are accessed centrally via [FloxHub][floxhub] and managed using the Flox CLI.

In the [introduction][intro] we discussed how annotations are used to tell Imageless Kubernetes which Flox environment to run.
However, we assumed that the referenced environment was publicly available without authentication.
If you plan to use private environments, you will have to authenticate Imageless Kubernetes using your FloxHub user credentials.

To do so, you need to first login to FloxHub using the Flox CLI using [`flox auth login`][flox_auth], if you haven't done so already.
You then create a new Kubernetes secret:

```bash
flox auth token \
  | kubectl create secret generic floxhub-token \
    --from-file=floxhub-token=/dev/stdin
```

    Tokens generated with `flox auth token` are associated with your user account and will expire 1 month from when they were issued. For a more robust alternative see [Machine Access Tokens for Organizations](../concepts/organizations.md#machine-access-tokens).

    The user creating the token via `flox auth token` will need at least version 1.7.6 of the Flox CLI.

Finally, you add a secret volume to your pod specification and mount it to `/var/run/secrets/flox.dev` inside your container.

A sample specification is shown below:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: flox-containerd-demo
  annotations:
    flox.dev/environment: "flox/echoip"
spec:
  runtimeClassName: flox

  # Required for auth: a secret volume referencing the secret created with
  # `$ kubectl create secret`
  volumes:
    - name: secret-volume
      secret:
        secretName: floxhub-token

  containers:
    - name: empty
      image: flox/empty:1.0.0
      command: ["echoip"]

      # Required for auth: mount the secret into a known place where Imageless Kubernetes can read it.
      volumeMounts:
        - name: secret-volume
          mountPath: "/var/run/secrets/flox.dev"
          readOnly: true
```

## Telemetry

Since Imageless Kubernetes uses the Flox CLI to perform certain operations such as activating your environment, Imageless Kubernetes will report the same telemetry by default that the Flox CLI reports.
This includes information such as:

- Which subcommands were run
- Which shell was used for the activation (Bash, Zsh, etc)
- Whether the environment was remote (e.g. stored on FloxHub) or not
- etc

We also use Sentry for error reporting.
This information helps us focus feature development and maintenance on the areas that deliver the most value for our users.

However, we understand that some users either don't want any information collected or work in an environment that does not allow this kind of information to be collected.
For this reason we offer the ability to disable telemetry.

### Disabling telemetry

When using the Flox CLI directly you can set `FLOX_DISABLE_METRICS=1` in your environment.
With Imageless Kubernetes, you can set an annotation on the pod specification to accomplish the same goal.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: flox-containerd-demo
  annotations:
    flox.dev/environment: "flox/echoip"
    # Disable telemetry
    flox.dev/disable-metrics: "true"
spec:
  runtimeClassName: flox
  containers:
    - name: empty
      image: flox/empty:1.0.0
      command: ["echoip"]
```

## Activation mode

By default, Imageless Kubernetes pods start in `run` mode. `run` mode is intended only to run packages installed in the Flox environment, but not provide any of the installed development dependencies.

The `flox.dev/activate-mode` annotation can be used to configure the mode, which may be useful for applications such as running CI jobs in Flox-enabled pods.

See the [`options.activate.mode`](../man/manifest.toml.md#options) option in the manifest for more details on modes.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: quotes-app
  annotations:
    flox.dev/environment: "flox/quotes-app"
    # Activate in dev mode
    flox.dev/activate-mode: "dev"
```

## Generations

A specific [generation][generations] of an environment on FloxHub can be specified as part of the `flox.dev/environment` annotation.
This can be useful to pin a specific version of an environment to allow for intentional or staged upgrades.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: quotes-app
  annotations:
    # Pin to generation 2 of the environment
    flox.dev/environment: "flox/quotes-app:2"
```

## Mutability

By default, Imageless Kubernetes pods are immutable, such that `flox install` commands are not possible and `/nix` is mounted read-only.

To enable mutability (e.g. for debugging), the `flox.dev/nix-mutable` annotation can be used.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: quotes-app
  annotations:
    flox.dev/environment: "flox/quotes-app"
    # Enable /nix mutability
    flox.dev/nix-mutable: "true"
```

## Mixed Flox/non-Flox pods

Imageless Kubernetes allows mixing Flox and non-Flox-based containers in the same pod, supporting the use of conventional init or sidecar containers combined with Flox-based workloads.
This is accomplished through the use of two annotations: `flox.dev/skip-containers` and `flox.dev/skip-containers-exec`.

`flox.dev/skip-containers` accepts a comma-separated list of containers that will _not_ be modified by the Flox runtime, and will be run as if they were started with the default runtime (e.g. `runc`). This option is best used for sidecars like `vault-agent` or `istio` that should run completely unmodified.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: quotes-app
  annotations:
    vault.hashicorp.com/agent-inject: "true"
    vault.hashicorp.com/role: "myapp-role"
    flox.dev/environment: "flox/quotes-app"
    # Keep these containers unmodified
    flox.dev/skip-containers: "vault-agent,vault-agent-init"
  spec:
    containers:
...
    - name: vault-agent
      image: hashicorp/vault:latest
      command: ["/bin/sh", "-ec"]
      args:
      - |
        vault agent -config=/vault/configs/agent.hcl
      env:
      - name: VAULT_ADDR
        value: "http://vault.vault.svc.cluster.local:8200"
      volumeMounts:
      - name: vault-secrets
        mountPath: /vault/secrets

    - name: quotes-app
      image: flox/empty:1.0.0
      command: ["quotes-app-go"]
      volumeMounts:
      - name: vault-secrets
        mountPath: /vault/secrets
        readOnly: true
...
```

`flox.dev/skip-containers-exec` also accepts a comma separated list of containers, but containers specified in this annotation _will_ contain the Flox environment specified in `flox.dev/environment`.

The difference from `skip-containers` is that while `skip-containers-exec` containers will have their main process run from the Flox environment, commands run via `kubectl exec` or equivalent will be run outside of it. This option is best used when you want the container's main workload to run in the Flox environment, but need exec commands (for debugging, health checks, or auxiliary tasks) to run in the base container environment without Flox.

[intro]: ./intro.md
[floxhub]: ../concepts/floxhub.md
[flox_auth]: ../man/flox-auth.md
[generations]: ../concepts/generations.md

---


## Flox + CUDA tutorial

> Source: `tutorials/cuda.md`

---
title: Flox + CUDA tutorial
description: It's easy to install and use the CUDA Toolkit with Flox
---

# Flox + CUDA tutorial

Flox is a next-generation, language-agnostic package and environment manager.

With Flox you get reproducible collections of tools, environment variables, services, and setup scripts
in the form of carefully configured subshells.
There's no container isolation preventing you from using your favorite shell, painstakingly crafted
dotfiles, or favorite utilities.
Since Flox "environments" are reproducible, you get the same exact setup no matter where you use it,
whether that's local development, in CI, bundled into a container, or deployed as a service on a
virtual machine.
With Flox, "works on my machine" problems are a thing of the past.

Flox is officially licensed to distribute NVIDIA's [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit),
which provides libraries for fully utilizing the computational power of NVIDIA GPUs for a variety of
workloads, including AI, scientific research, and other enterprise applications.

Figuring out the compatibility matrix between an upstream package that depends on CUDA, the CUDA
Toolkit itself, and any other dependencies required for the package can be a big time investment.
Flox makes that process easier by only requiring you to do the work once.
Once the environment is built, anyone on Linux or Windows Subsystem for Linux gets exactly the same
set of tools and dependencies.
If that wasn’t cool enough, with Flox each project can have a different CUDA Toolkit installed with
causing version conflicts.
Each project’s dependencies are completely independent of one another.

For a quick overview of Flox, see [Flox in 5 Minutes](https://flox.dev/docs/flox-5-minutes/).
Otherwise, let's see how easy it is to install and use the CUDA Toolkit with Flox.

## Official CUDA examples

The [flox/cuda-samples](https://github.com/flox/cuda-samples) repository is a fork of the
`NVIDIA/cuda-samples` repository, and contains a variety of small projects demonstrating different
aspects and capabilities of the CUDA Toolkit.
We've added a Flox environment on the `flox-env` branch that contains the dependencies for all
examples in this repository.
If you already have Flox installed, getting up and running is *very* easy:

```{ .bash .copy }
git clone https://github.com/flox/cuda-samples.git
cd cuda-samples
git checkout flox-env
flox activate

```

This may take some time because the download is quite large (~9GB), but that's because the full CUDA
Toolkit is quite large and the examples in this repository demonstrate many of its capabilities.
The upside is that the CUDA Toolkit in the Flox Catalog is broken into components, so for *your*
applications you can install the minimal subset that you need and download much less.
For example, to install the latest `nvcc` you would run `flox install flox-cuda/cudaPackages.cuda_nvcc`.

Furthermore, since each Flox environment is scoped to a particular directory, you can have
projects in different directories on your system that use and install completely different
versions of the CUDA Toolkit with no problems at all.

Let's pick one of the examples and build it.

### HSOpticalFlow example

Navigate to the `Samples/5_Domain_Specific/HSOpticalFlow` directory.
This example runs headless in your terminal, but don't worry, we'll get to some nice visuals in a moment.

First let’s build the example (note that `make -j8` builds the example with 8 jobs, but you may want
more or less depending on how many CPU cores are available on your machine):

```console
mkdir build && cd build && cmake .. && make -j8
```

Now let’s run the program:

```console
$ ./HSOpticalFlow
HSOpticalFlow Starting...

GPU Device 0: "Ada" with compute capability 8.9

Loading "frame10.ppm" ...
Loading "frame11.ppm" ...
Computing optical flow on CPU...
Computing optical flow on GPU...
L1 error : 0.044308

```

And with that you've run your first CUDA-enabled project! Your output may look slightly differently,
but this example should run on NVIDIA GPUs dating back to the GTX 750 released in 2014.

The Flox environment in this repository includes all of the dependencies necessary for any of the
examples with a few exceptions:

- Flox doesn't run natively on Windows (only through WSL2), so the dependencies for the native
  Windows examples are skipped.
- The NvSci example is skipped because NvSci functionality is only included in NVIDIA Drive OS
  distributions of the CUDA Toolkit.

This means you needed *and were given* CMake, Make, GCC, OpenGL libraries, Vulkan libraries, etc,
(*and* the CUDA Toolkit) without needing to figure that out on your own. Whoever prepared the
environment took care of that for you.

Just `git clone` and `flox activate` and you're up and running.

If you’d like to explore some of the other examples, the `mkdir build && ...` command is what you'll
run from inside an example directory the first time you want to build it. Feel free to play around!

### Julia set

Now we're going to generate a rendering of the [Julia set](https://en.wikipedia.org/wiki/Julia_set).
Navigate to `Samples/5_Domain_Specific/Mandelbrodt` then run the following commands:

```{ .bash .copy }
mkdir build && cd build && cmake .. && make -j8
./Mandelbrodt

```

This will open a window with a rendering of the [Mandelbrodt set](https://en.wikipedia.org/wiki/Julia_set),
and display some instructions for tweaking the output.
Press the `J` key to switch from the Mandelbrodt set to the Julia set, then play around with colors.
Here's an example of what the output can look like after tweaking some of the parameters.
![julia_set.png](julia_set.png)

## PyTorch

Not only can you build against the CUDA Toolkit itself, but with Flox any package that *depends* on
CUDA can be installed with CUDA acceleration automatically enabled.
To demonstrate this, we'll build and run an example from the [PyTorch examples repository](https://github.com/pytorch/examples),
and this time we'll build the environment from scratch to see how easy it is.

Clone the PyTorch repository, navigate to the `mnist` example, and create a Flox environment in it:

```{ .bash .copy }
git clone <https://github.com/pytorch/examples.git> pytorch-examples
cd pytorch-examples/mnist
flox init

```

At this point the Flox CLI will ask to install some packages for you, but in this case we want to say
**no** because we'll select some different packages. Normally this is helpful and saves you time
installing common packages for a given language ecosystem, but in this case we’re going to install
some specific packages that have CUDA acceleration automatically enabled.

In this case we'll install the following packages:

```console
$ flox install python3 flox-cuda/python3Packages.torch flox-cuda/python3Packages.torchvision
✅ 'python3' installed to environment 'mnist'
⚠️  'torch' installed only for the following systems: x86_64-linux, aarch64-linux
⚠️  'torchvision' installed only for the following systems: x86_64-linux

```

Now let's activate the environment and ensure that our CUDA installation is properly detected:

```console
$ flox activate
$ python -c "import torch; print(torch.cuda.is_available())"
True

```

Now we can run the example to classify handwritten digits in the MNIST database:

```console
$ python main.py
100.0%
100.0%
100.0%
100.0%
Train Epoch: 1 [0/60000 (0%)]   Loss: 2.299823
Train Epoch: 1 [640/60000 (1%)] Loss: 1.745035
Train Epoch: 1 [1280/60000 (2%)]        Loss: 0.988044
Train Epoch: 1 [1920/60000 (3%)]        Loss: 0.612987
Train Epoch: 1 [2560/60000 (4%)]        Loss: 0.333546
Train Epoch: 1 [3200/60000 (5%)]        Loss: 0.341566
...
Train Epoch: 14 [58880/60000 (98%)]     Loss: 0.032806
Train Epoch: 14 [59520/60000 (99%)]     Loss: 0.014871

Test set: Average loss: 0.0256, Accuracy: 9919/10000 (99%)

```

99% accuracy, nice!

This example took a little over 1 minute to run on a machine with an NVIDIA RTX 4090.

## Conclusion

As you can see, getting started with Flox and CUDA is very straightforward.
Installing the CUDA Toolkit for your project is just as easy as installing any other package.
On top of that, installing a particular CUDA stack is extremely easy.

---


## The default environment

> Source: `tutorials/default-environment.md`

---
title: The default environment
description: Using Flox as your system package manager
---

# The default environment

In the typical development case you would create a directory for your project.
`flox init` to create an environment for it,
then `flox activate` in that directory when you want to work on that project.
The packages in that environment are available when the environment is active,
and they're unavailable otherwise.
But what about packages that you _always_ want available?

Without Flox, you may turn to your system's package manager
(`apt`, `yum`, `brew`, etc)
in order to install packages system-wide.
This has a number of drawbacks:

- You often only have a single package version to choose from.
- You often can't install multiple versions side-by-side.
- You can't ensure that multiple machines get the exact same version.
- You may not be able to back up the list of installed packages.

The Flox `default` environment doesn't have these problems,
so let's take a look at how to set it up.

## Initial setup

At the most basic level, the `default` environment is simply an environment
called `default`.
`default` environments are typically [shared via FloxHub][floxhub-env];
We refer to the one associated with your account,
as _your_ `default` environment.

In some cases Flox will prompt to set up your `default` environment for you.
To create the `default` environment yourself,
make sure you are logged in to FloxHub,
and initialize a FloxHub environment under your account:

```{ .bash }
flox auth status || flox auth login
✅ Authentication complete
✅ Logged in as <youruser>

flox init -r <youruser>/default
```

Once the environment has been created,
you'll want to configure your shell to activate the environment with every new
shell.
This can be done as part of the automatic setup,
or you can add a single line to your shell's RC file:

=== "Bash"

    Depending on the context, Bash will load different startup files.
    For that reason, we need to add a line to two different files:
    `.bashrc` and `.profile`.
    Add the following line to the very end of each of those files:

    ```{ .bash .copy }
    eval "$(flox activate -r <your username>/default -m run)"
    ```

=== "Zsh"

    Add the following line to the very end of your `.zprofile` and `.zshrc`
    files:

    ```{ .zsh .copy }
    eval "$(flox activate -r <your username>/default -m run)"
    ```

=== "Fish"

    Add the following line to the very end of your `config.fish` file:

    ```{ .fish .copy }
    flox activate -r <your username>/default -m run | source
    ```

=== "Tcsh"

    Add the following line to the very end of your `.tcshrc` file:

    ** For FloxHub environments:**

    ```{ .tcsh .copy }
    eval "`flox activate -r <your username>/default -m run`"
    ```

---

Once you've added that line to your shell,
you'll need to restart your shell (or open a new one) for the changes to
take effect.
If you don't want to activate it automatically, the default
environment can simply be activated using `-d` parameter of the Flox CLI
like so:

```{ .bash .copy }
flox activate -r <your username>/default
```

## Taking it for a spin

Now let's test out your new `default` environment.
If you're in an arbitrary directory and `apt install hello` you would expect
it to be available no matter what directory you're in.
Let's do the same with Flox.

Let's create a new temporary directory that we know doesn't have an environment in it.

```{ .bash .copy }
cd $(mktemp -d)
```

Now we'll install a package and see that it gets installed to the `default`
environment,
like you would expect from your system's package manager:

```console
$ flox install hello
✅ 'hello' installed to environment 'default'
```

It worked (though you shouldn't be surprised; Flox is awesome)!

## Installing packages to the default environment from another Flox environment

If you're in a project directory with an existing Flox environment,
unsurprisingly, running `flox install <pkg>` will install the package
to the environment in that directory, rather than your default environment.

Nevertheless, it's still easy to install whatever you wish to your `default`
environment.
All you need to do is pass the `-d` argument to the `install` command, like so:

```{ .bash .copy }
flox install -r <your username>/default ~ hello
```

When you do this, you should see the following output, indicating success:

```console
✅ 'hello' installed to environment 'default'
```

## Customization

Depending on when you created your default environment
(the default was changed recently),
you may also see `flox [default]` as part of your prompt for every new shell.
You can configure that with a single command:

=== "Do show the Flox prompt"

    ```{ .bash .copy }
    flox config --set hide_default_prompt false
    ```

=== "Don't show the Flox prompt"

    ```{ .bash .copy }
    flox config --set hide_default_prompt true
    ```

---

## Sharing

Since the `default` environment is "just" another [FloxHub environment][floxhub-env],
it's possible to push this environment and share it between machines.

In fact, activating or initializing default environments on other machines
will link to the environment that is already on FloxHub.
To use the environment on other machines simply log in
and add the activation to your dotfiles as described above.

Changes made to the environment locally (e.g. newly installed packages) can be synchronized
with [`flox push`][push] and [`pull`][pull].

---

## Generations

Pushing an environment creates the first version of the environment tracked on
FloxHub, which is called a generation.

To see how generations can be used to undo changes, edit the environment,
perhaps adding a variable `FOO = "bar"` to the `[vars]` section.
Then push the environment to FloxHub:

```{ .sh .copy }
flox edit;
flox push
```

This should print a link to your environment on FloxHub.
Follow the link and click the `Generations` tab.
This should show the most recent generation created by the `flox edit` command.

To revert to the version of the environment prior to the edit, run rollback:

```{ .sh .copy }
flox generations rollback;
flox push
```

Now if you run `flox pull` on another host, you'll get the rolled-back
environment, without the edit.

---

## Conclusion

Whether you want a reproducible package manager for your whole system,
or you want reproducible, cross-platform developer environments,
Flox has you covered.
Even better, if you want both a package manager _and_ developer environments,
with Flox you only need to learn one tool.

---

## Detached and directory based `default` environments

Since `default` environments are normal Flox environments,
you can use any other environment the same way.

For example you can

=== "initialize a local environment e.g. in your home directory"

```{ .bash .copy }
flox init -d ~
```

=== "start with a template on FloxHub"

```{ .bash .copy }
flox pull --copy -d ~ owner/name
```

=== "use a directory based FloxHub environment"

```{ .bash .copy }
flox pull -d ~ owner/name
```

---

If you choose to automatically activate the environment in your rc files,
change the `flox activate -r <youruser>` accordingly
to e.g. `flox activate -d ~`.

[auth]: ../man/flox-auth.md
[init]: ../man/flox-init.md
[push]: ../man/flox-push.md
[pull]: ../man/flox-pull.md
[floxhub-env]: ./sharing-environments.md

---


## adjust this to match your existing or desired node group configuration -- below values are examples

> Source: `k8s/install/eks.md`

---
title: "Amazon EKS"
description: "Installing Imageless Kubernetes to Amazon EKS"
---

If you have an existing EKS cluster, we recommend creating a new node group specifically for Imageless Kubernetes.

This guide will walk through the steps needed to create the node group and configure the cluster with both [Terraform][terraform] and [eksctl][eksctl].

To run on EKS, each node in the node group will need to:

- Install Flox
- Install the Flox `containerd` runtime shim
- Register the shim with `containerd`
- Register the shim with Kubernetes

Most of this can be done as part of the node bootstrapping process, using custom user data to pass instructions to [nodeadm][nodeadm].

If you would like to create a new cluster for Imageless Kubernetes, examples are available on [GitHub][k8s-shim-install].

    Additional information on `nodeadm` and bootstrapping with user data can be found in the [EKS documentation][userdata-docs].

--8<-- "k8s-shim-cli-version.md"

    The following examples are tailored towards adding node groups to existing clusters -- complete examples for creating new clusters with Imageless Kubernetes are available on [GitHub][k8s-shim-install].

## Node Configuration via Terraform

### Terraform Prerequisites

To create the node group, you will need:

- Subnets for the node group to use
- IDs for cluster and node security groups
- The cluster's service CIDR (i.e. the range from which cluster services will receive IPs)

If you've used a public module such as [terraform-aws-eks][terraform-aws-eks], most of these details should be available either from the module configuration or outputs.

### Terraform node group creation

This example will use the [eks-managed-node-group][eks-managed-node-group] submodule of [terraform-aws-eks][terraform-aws-eks], but it can also be used standalone, regardless of how the cluster was defined in Terraform.

The following Terraform configuration can be used to provision a node group with the Flox runtime; see comments for guidance on each input.
This example assumes you already have Terraform configuration for a cluster including the [AWS provider][aws-tf-provider].

    See the [upstream module documentation][terraform-aws-eks] for details on adding this node group to an autoscaling scheme (e.g. Cluster Autoscaler, Karpenter).

```hcl title="nodegroup.tf"
module "eks_managed_node_group" {
  source  = "terraform-aws-modules/eks/aws//modules/eks-managed-node-group"
  version = "21.6.1" # tested with this version, but only >=21 required

  name         = "flox"
  cluster_name = "my-cluster"

  # replace with your node subnets
  subnet_ids = ["subnet-01982749e3b6e77a6", "subnet-025dd07e5117afef5", "subnet-0b0ef36fe25286a83"]

  # replace with your desired instance types -- x86_64 or ARM (Graviton) are supported
  instance_types = ["t3.small"]

  cluster_primary_security_group_id = module.eks.cluster_primary_security_group_id
  vpc_security_group_ids            = [module.eks.node_security_group_id]
  cluster_service_cidr              = module.eks.cluster_service_cidr

  ami_type     = "AL2023_x86_64_STANDARD" # set depending on CPU architecture
  desired_size = 1
  min_size     = 0
  max_size     = 10

  # required if you need non-default disk settings; disk_size parameter cannot be used with cloudinit_pre_nodeadm
  block_device_mappings = {
    xvda = {
      device_name = "/dev/xvda"
      ebs = {
        volume_size           = 50
        volume_type           = "gp3"
        encrypted             = true
        delete_on_termination = true
      }
    }
  }

  # needed to pair with the RuntimeClass to ensure Flox pods only get scheduled here
  labels = {
    "flox.dev/enabled" = "true"
  }

  cloudinit_pre_nodeadm = [
    {
      content_type = "text/x-shellscript; charset=\"us-ascii\""
      content      = <<-EOT
            #!/bin/bash
            dnf install -y https://flox.dev/downloads/yumrepo/flox.x86_64-linux.rpm
            flox activate -r flox/containerd-shim-flox-installer --trust
          EOT
    },
    {
      content_type = "application/node.eks.aws"
      content      = <<-EOT
            ---
            apiVersion: node.eks.aws/v1alpha1
            kind: NodeConfig
            spec:
              cluster: {}
              containerd:
                config: |
                  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.flox]
                    # Our shim is a build of the runc shim with hooks, so override runtime_path
                    # here but otherwise obey all the runc protocol specifications.
                    runtime_path = "/usr/local/bin/containerd-shim-flox-v2"
                    runtime_type = "io.containerd.runc.v2"
                    # Whitelist all annotations starting with "flox.dev/"
                    pod_annotations = [ "flox.dev/*" ]
                    container_annotations = [ "flox.dev/*" ]
                  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.flox.options]
                    SystemdCgroup = true
              instance:
                localStore: {}
              kubelet: {}
          EOT
    }
  ]
}
```

In the above example, the `cloudinit_pre_nodeadm` section is used by `nodeadm` to bootstrap the node as it starts up.

First, it installs Flox on the node using the latest `rpm` package, which will then be used to create pods backed by Flox environments.

Then, the `flox activate` command executes an [installer][shim-installer] that detects the node's running `containerd` version, downloads the correct version of the Flox runtime shim to match, and installs it to `/usr/local/bin` on the node.

Finally, it uses a `NodeConfig` manifest to leverage `nodeadm`'s native functionality to update the node's `containerd` configuration to be aware of the Flox runtime.

The `labels` section is used to give each Flox-enabled node an identifier to ensure that Flox pods only target these nodes.
The `label` is used in concert with a `RuntimeClass` in the next section to make Kubernetes aware of the Flox runtime.

## Node Configuration via eksctl

For clusters created using methods other than Terraform (e.g. AWS management console), we recommend using [eksctl][eksctl] to create the Flox node group.

`eksctl` is a utility developed by AWS to create and manage EKS clusters, including clusters it did not create.

For our purposes, `eksctl` greatly simplifies appending custom configuration to the base launch template.

### eksctl Prerequisites

- A running EKS cluster with at least one existing node group
- List of VPC subnet IDs to be used for the new node group
- Connectivity to the cluster API (i.e. `kubectl` is usable)

### Installation

#### Cluster access

First, install `eksctl` and ensure that you have access to the cluster:

- Install `eksctl` (e.g. `flox install eksctl`).
- Set AWS credentials in your environment (e.g. copy `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` from management console).
- Run `eksctl get cluster` and ensure the cluster is visible via the command below.


```sh
❯ eksctl get cluster
NAME		REGION		EKSCTL CREATED
flox	    us-east-1	True
```

#### eksctl node group creation

Next, we'll create a `ClusterConfig` manifest that will be used to create the Flox node group.

    See the [eksctl documentation][eksctl-docs] for guidance on additional parameters such as IAM configuration and autoscaler support.

Apply the below `ClusterConfig` with `eksctl create nodegroup -f nodegroup.yaml`. You can also visualize the changes before deployment with `eksctl create --dry-run`.

```yaml title="nodegroup.yaml"
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: flox # name of the target cluster for this node group
  region: us-east-1

# adjust this to match your existing or desired node group configuration -- below values are examples
managedNodeGroups:
  - name: flox
    instanceType: t3.small # choose your desired instance type
    amiFamily: AmazonLinux2023
    desiredCapacity: 1
    minSize: 0
    maxSize: 10
    labels:
      flox.dev/enabled: "true" # used in RuntimeClass to ensure flox workloads only get scheduled on these nodes
    preBootstrapCommands:
      - |
         dnf install -y https://flox.dev/downloads/yumrepo/flox.x86_64-linux.rpm
         flox activate -r flox/containerd-shim-flox-installer --trust
    overrideBootstrapCommand: |
      apiVersion: node.eks.aws/v1alpha1
      kind: NodeConfig
      spec:
        containerd:
          config: |
            [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.flox]
              # Our shim is a build of the runc shim with hooks, so override runtime_path
              # here but otherwise obey all the runc protocol specifications.
              runtime_path = "/usr/local/bin/containerd-shim-flox-v2"
              runtime_type = "io.containerd.runc.v2"
              # Whitelist all annotations starting with "flox.dev/"
              pod_annotations = [ "flox.dev/*" ]
              container_annotations = [ "flox.dev/*" ]
            [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.flox.options]
              SystemdCgroup = true

 # required if cluster was not created with eksctl, see https://docs.aws.amazon.com/eks/latest/eksctl/unowned-clusters.html#create-nodegroup
 vpc:
  id: "vpc-12345"
  securityGroup: "sg-12345"    # this is the ControlPlaneSecurityGroup
  subnets:
    # should match the IDs of subnets attached to existing node group
    private:
      private1:
        id: "subnet-12345"
      private2:
        id: "subnet-67890"
    public:
      public1:
        id: "subnet-12345"
      public2:
        id: "subnet-67890"
```

Further explanation of the bootstrapping process is available in the Terraform section above.

## Kubernetes Configuration

A [RuntimeClass](https://kubernetes.io/docs/concepts/containers/runtime-class/) is used to expose the runtime to Kubernetes such that it can be utilized to create pods.
The `RuntimeClass` needs to be applied to the cluster, where the `nodeSelector` matches the `label` given to the node group above

```yaml title="RuntimeClass.yaml"
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: flox
handler: flox
scheduling:
  nodeSelector:
    flox.dev/enabled: "true"
```

which can be applied by `kubectl apply -f RuntimeClass.yaml`.

The `nodeSelector` ensures that Flox pods will only be scheduled on nodes with the Flox runtime installed.

## Conclusion

Once the node group is running, you are ready to create pods using the Flox runtime.

A sample `Pod` manifest is available in the [Introduction][intro-section], but any Kubernetes resource that creates a pod (e.g. `Deployment`) can be used by setting the `runtimeClassName` parameter to `flox`.

[intro-section]: ../intro.md
[eksctl]: https://docs.aws.amazon.com/eks/latest/eksctl/
[eksctl-docs]: https://docs.aws.amazon.com/eks/latest/eksctl/nodegroup-managed.html
[terraform]: https://developer.hashicorp.com/terraform
[terraform-aws-eks]: https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest
[eks-managed-node-group]: https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest/submodules/eks-managed-node-group
[userdata-docs]: https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html#launch-template-user-data
[nodeadm]: https://github.com/awslabs/amazon-eks-ami/blob/main/nodeadm
[shim-installer]: https://hub.flox.dev/flox/containerd-shim-flox-installer
[aws-tf-provider]: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
[k8s-shim-install]: https://github.com/flox/flox-containerd-shim-deploy

---


## Flox in 5 minutes

> Source: `flox-5-minutes.md`

---
title: Flox in 5 minutes
description: Get started with creating Flox environments.
---

# Flox in 5 minutes

Flox is a next-generation, language-agnostic package and environment manager.
With it you create sets of tools, environment variables, and setup scripts that work reproducibly from machine to machine, x86_64 to Arm, and macOS to Linux.
The best part is that all of this works without causing version conflicts between projects.

We call these stacks **Flox environments**.
Flox environments are based on carefully configured subshells, so there's no container isolation preventing you from using your favorite tools or artisanally handcrafted dotfiles.
Even better, these environments _compose_ and _layer_ so you can prepare different environments
for different needs and combine them to seamlessly work across different contexts.

Finally, you can use Flox environments for local development, CI, and production to ensure that you have a consistent set of software across the entire software development lifecycle.

Buckle up, it's time for a whirlwind tour of Flox.

## Get the project

We've prepared a sample project for you, but you'll need to [install Flox][install_flox] to follow along.
Once you have Flox, you can clone the project:

```{ .bash .copy }
git clone https://github.com/flox/flox-in-5min.git
cd flox-in-5min
```

## Tools prepared for you

Once you have the project, you can run the [`flox activate`][activate] command to enter the environment:

```{ .console }
$ flox activate
✅ You are now using the environment 'flox-in-5min'.
To stop using this environment, type 'exit'
```

You now have all of the dependencies needed to follow along.
To prove it, run the following command:

```{ .console }
$ go run main.go
Hello from Flox!
```

Whoever prepared this environment knew that you needed a Go toolchain in order to work on the project, so they included a Go toolchain in the Flox environment.
_**This is the magic of Flox.**_

To get to work on an existing project you need two commands: `git clone` and `flox activate`.
Onboarding a new engineer now has one step: install Flox.
No more `README.md` with a list of libraries you need install.
No more `setup.sh`.
Time not spent installing tools and solving dependency conflicts is time spent getting to know the team and the project.

Now let's see what else is installed to the environment with the [`flox list`][list] command:

```{ .console }
$ flox list
bun: bun (1.2.20)
coreutils: coreutils (9.7)
go: go (1.24.5)
nasm: nasm (2.16.03)
nodejs_24: nodejs_24 (24.5.0)
```

That's right, not only do you have Go installed, you also have a cutting edge Javascript toolchain with [Bun][bun].
Since Flox is language agnostic, you can use one tool (Flox) to manage your entire stack of developer tools.
This environment covers the full stack, from a [Zig][zig]-powered Javascript bundler and runtime at the top of the stack, to an assembler like `nasm` at the very bottom of the stack.

This environment is also reproducible, meaning that anyone that runs `flox activate` will get exactly the same set of tools, and that's super important!
You'd think that something as simple as the `sleep` command wouldn't cause problems, but `/bin/sleep infinity` will sleep for a surprisingly short time on macOS (ask us how [we know][sleep-issue]).
Ensuring that everyone is using the _exact_ same packages prevents wasted time and subtle bugs.

## Finding packages

Let's say we want a new package: `ripgrep`.

```{ .console }
$ flox search ripgrep
ripgrep                           Utility that combines the usability of The Silver Searcher with the raw speed of grep
ripgrep-all                       Ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, and more
emacsPackages.ripgrep             <no description provided>
vimPlugins.blink-ripgrep-nvim     <no description provided>
emacsPackages.projectile-ripgrep  <no description provided>
vgrep                             User-friendly pager for grep/git-grep/ripgrep
repgrep                           Interactive replacer for ripgrep that makes it easy to find and replace across files on the command line
grip-grab                         Fast, more lightweight ripgrep alternative for daily use cases
bat-extras.batgrep                Quickly search through and highlight files using ripgrep

Use 'flox show <package>' to see available versions
```

Cool, what if I want a specific version?

```{ .console }
$ flox show ripgrep
ripgrep - Utility that combines the usability of The Silver Searcher with the raw speed of grep
    ripgrep@14.1.1
    ripgrep@14.1.0
    ripgrep@14.0.3
    ripgrep@14.0.1
    ripgrep@13.0.0
    ripgrep@12.1.1 (aarch64-linux, x86_64-darwin, x86_64-linux only)
```

To install it you would run

```{ .bash .copy }
flox install ripgrep
```

## What else can Flox do?

Your environment is stored as a `.flox` directory in your repository, but you can also [`push`][push] it to [FloxHub][floxhub] to make it centrally managed and available from anywhere.
We only have 5 minutes, so we're going to skip over that for now, but see the [sharing environments tutorial][sharing] for more information.

The configuration for your environment is called the ["manifest"][manifest], a TOML file stored at `.flox/env/manifest.toml`.
You can print it with `flox list -c` or edit it with [`flox edit`][edit].

Let's take a look at this manifest:

```{ .bash .copy }
flox list -c
```

```{ .toml .copy }
version = 1

[install]
go.pkg-path = "go"
nodejs_24.pkg-path = "nodejs_24"
ripgrep.pkg-path = "ripgrep"
coreutils.pkg-path = "coreutils"
bun.pkg-path = "bun"
nasm.pkg-path = "nasm"

[vars]
MY_VAR = "pretty neat"

[services.stopwatch]
command = '''
  while true; do date; sleep 5; done
'''
```

Pretty straightforward.
Packages go in `[install]`, and maybe the syntax is a little funky, but that's for a good reason we don't have time to get into.
See [this page][install-section] for more details about the various things you can specify about a package.

What are these `[vars]` and `[services]` sections?

The `[vars]` section defines environment variables you want set in your shell after running `flox activate`.
See for yourself:

```{ .console }
$ echo "$MY_VAR"
pretty neat
```

Imagine using this to set a port number or some other configuration value.

The `[services]` section is how you define background processes for your environment, like a web server or a database.
Start the `stopwatch` service with the `flox services start` command:

```{ .console }
$ flox services start
✅ Service 'stopwatch' started.
```

Let's make sure it's running:

```{ .console }
$ flox services status
NAME       STATUS       PID
stopwatch  Running    51774
```

Now let's see its logs:

```{ .console }
$ flox services logs --follow
stopwatch: Fri Aug 22 19:17:30 MDT 2025
stopwatch: Fri Aug 22 19:17:35 MDT 2025
stopwatch: Fri Aug 22 19:17:40 MDT 2025
stopwatch: Fri Aug 22 19:17:45 MDT 2025
stopwatch: Fri Aug 22 19:17:50 MDT 2025
stopwatch: Fri Aug 22 19:17:55 MDT 2025
stopwatch: Fri Aug 22 19:18:00 MDT 2025
stopwatch: Fri Aug 22 19:18:05 MDT 2025
```

This service prints the current time every 5 seconds, which you can see defined in the `services.stopwatch.command` field of the manifest.
Press `Ctrl-C` to stop watching the logs, unless you really enjoy that for some reason.
We don't want the service to run forever, so let's stop it with the `flox services stop` command.

```{ .console }
$ flox services stop
✅ Service 'stopwatch' stopped
```

A _really cool_ feature of Flox is that if you were to exit the environment by running `exit` or pressing `Ctrl-D`, the services running in the environment would be automatically stopped.
This feature has given our engineers gray hair, but we think the dopamine hit is worth it.
If you want services to start when you enter the environment, you can use the `-s/--start-services` option when running `flox activate`.

## Customizing your shell

To wrap things up, let's say you want to set some project-specific aliases.
Run `flox edit` and add this to the bottom of your manifest:

```{ .toml .copy }
[profile]
bash = '''
  alias sayhi="echo 'Hello there, bash user'"
'''
zsh = '''
  alias sayhi="echo 'Hello there, zsh user'"
'''
# The superior shell
fish = '''
  alias sayhi "echo 'Hello there, fish user'"
'''
# Hello from 1989
tcsh = '''
  alias sayhi "echo 'Hello there, tcsh user'"
'''
```

Now if you exit the Flox environment via `Ctrl-D` or `exit` and reactivate via `flox activate`, you'll have a wonderful new shell alias called `sayhi`:

```{ .console }
$ sayhi
Hello there, fish user
```

There is a wealth of ways that you can customize the shell environment inside of your Flox environment.
See the [customizing the shell enviroment tutorial][activation-tutorial] for more information.

## But wait, there's more!

This probably took longer than 5 minutes, but hopefully changing the way you develop software was worth it.
There are _so_ many things we didn't have time to cover, so here's some additional reading material to keep you busy:

- [Designing cross-platform environments][multi-arch]
- [Running Flox in CI][ci]
- [Reusing and combining environments][composition] (modular developer environments!)
- [Replacing Homebrew with Flox][homebrew]
- [Build and publish packages with Flox][build-publish]

[install_flox]: ./install-flox/install.md
[create_guide]: ./tutorials/creating-environments.md
[sharing]: ./tutorials/sharing-environments.md
[init]: ./man/flox-init.md
[search]: ./man/flox-search.md
[show]: ./man/flox-show.md
[catalog]: ./concepts/packages-and-catalog.md
[install]: ./man/flox-install.md
[activate]: ./man/flox-activate.md
[edit]: ./man/flox-edit.md
[push]: ./man/flox-push.md
[list]: ./man/flox-list.md
[manifest]: ./man/manifest.toml.md
[multi-arch]: ./tutorials/multi-arch-environments.md
[services]: ./concepts/services.md
[bun]: https://bun.sh/
[zig]: https://ziglang.org/
[floxhub]: https://hub.flox.dev
[sleep-issue]: https://github.com/flox/flox/pull/1931
[install-section]: ./man/manifest.toml.md#install
[activation-tutorial]: ./tutorials/customizing-environments.md
[ci]: ./tutorials/ci-cd.md
[composition]: ./tutorials/composition.md
[homebrew]: ./tutorials/migrations/homebrew.md
[build-publish]: ./tutorials/build-and-publish.md

---


## Flox vs. container workflows

> Source: `concepts/flox-vs-containers.md`

---
Title: Flox vs. container workflows
Description: How does a Flox workflow differ from a container workflow?
---

# Flox vs. container workflows

Containers are everywhere these days.
They're the de-facto deployment method in the industry,
and they're often used for local development as well to ensure that every
developer gets the same environment.

Flox gives you these same benefits without many of the papercuts,
but the workflow is slightly different so it's worth exploring.

## Create a new development environment

Let's say you've created a new directory for your project,
`myproject`,
and entered it:

```{ .bash .copy }
mkdir myproject;
cd myproject
```

=== "Flox"

    Create a Flox environment for the project via [`flox init`][init]:

    ```{ .bash .copy }
    flox init
    ```

    This creates a `.flox` directory in `myproject`.
    At this point you can enter the environment,
    but it doesn't provide any new packages or functionality.

=== "Containers"

    Create a new `Dockerfile`.

    ```{ .bash .copy }
    touch Dockerfile
    ```

    At this point the `Dockerfile` isn't really useable since it doesn't say which
    image to build on top of (there's no `FROM` line).
    Let's pick the latest Ubuntu LTS release.

    ```{ .bash .copy }
    echo "FROM ubuntu:noble" >> Dockerfile
    ```

    This already adds some variability in that which image this refers to may
    change from moment to moment.

---

## Add packages

Now let's install some packages.
In a typical project there's usually different subsets of packages:

- Packages you don't care about too much, so the latest version will suffice.
- Packages whose versions you want pinned to a recent version.
- Packages that you're behind on updating because upgrading requires significant
  effort.

We'll pick a single package from each category:

- Latest is fine: `curl`
- Specific version: `yarn 1.22`
- Behind: `python3.10`

=== "Flox"

    This is pretty straightforward:

    ```{ .bash .copy }
    flox install curl yarn@1.22 python3@3.10
    ```

    Adding another package at a later date is as simple as running
    `flox install <package>` again.

=== "Containers"

    Add a `RUN` command to your `Dockerfile`:

    ```{ .dockerfile .copy }
    RUN apt update && apt install curl npm
    ```

    `yarn` will be installed via `npm`, so we include that in the `RUN` command.
    This version of Python isn't included in the Ubuntu 24.04 repositories,
    so you must install it from a Personal Package Archive (PPA).
    Do that with another `RUN` command:

    ```{ .dockerfile .copy }
    RUN sudo add-apt-repository ppa:deadsnakes/ppa -y && \
        sudo apt update && \
        sudo apt install python3.10
    ```

    This PPA is probably reputable, but now you're managing third-party package
    repositories.

    Adding another package at a later date requires editing the first `RUN`
    command.
    This requires rebuilding later layers,
    such as the one that installs `python3.10`.

---

## Configuration

What does it look like to configure your Flox environment compared to a
container?

A Flox environment is configured via a declarative TOML file called a
["manifest"][manifest].
The manifest for the environment created above looks like this:

```toml
version = 1

[install]
curl.pkg-path = "curl"
yarn.pkg-path = "yarn"
yarn.version = "1.22"
python3.pkg-path = "python3"
python3.version = "3.10"

[options]
systems = ["aarch64-darwin", "aarch64-linux", "x86_64-darwin", "x86_64-linux"]
```

One thing to note here is that the manifest defines a cross-platform environment
out of the box to ensure that there are no nasty surprises down the line.

A container is configured via a `Dockerfile`,
which is an imperative sequence of commands.

```{ .dockerfile .copy }
FROM ubuntu:noble

RUN apt update && apt install curl npm

RUN sudo add-apt-repository ppa:deadsnakes/ppa -y && \
    sudo apt update && \
    sudo apt install python3.10
```

The upside to a `Dockerfile` is that the commands are familiar
(e.g. `apt install`),
but the order of commands matters and you end up stuffing a lot of commands
into a single `RUN` command to avoid creating extra layers.

## Use the development environment

Let's say you want to do some work in the development environment.
With Flox you're put inside a subshell.
With containers you can use a shell inside the container or connect to the
running container via SSH.
However, with containers you also need to mount in your source code, etc.

=== "Flox"

    Activate the environment:

    ```console
    $ flox activate
    flox [myproject] $ # now you're in the environment
    ```

    Notice that there wasn't a separate "build" step.
    When you install, uninstall, or edit a Flox environment it's transactionally
    built to ensure that it's always working.

=== "Containers"

    First build the image:

    ```{ .bash .copy }
    docker build -t myproject .
    ```

    Then start the image (mounting your source) and create a shell inside of it:

    ```console
    $ docker run -v ./src:/src myproject -d --name myproject_container
    $ docker exec -it myproject_container bash
    $ # now you're inside the container
    ```

    Once you're inside the containers,
    you don't have any of your local tools, your shell's aliases,
    access to your dotfiles, or configurations for your local tools.

---

## Tear down the development environment

=== "Flox"

    This is pretty straightforward:

    ```console
    flox [myproject] $ exit
    ```

=== "Containers"

    This is pretty straightforward:

    ```console
    $ exit # leave the container shell
    $ docker stop myproject_container
    ```

---

## Perform initialization

Let's say you need to move some files around,
ensure a directory exists,
or some other kind of initialization before doing work inside the development
environment.

We'll do a pretend version of this by simply creating a directory `foo`.

=== "Flox"

    This would be performed in the `hook.on-activate` script that's run when
    activating your environment.
    You'll add this by first running `flox edit` and
    then modifying the `hook` section of your manifest to look like this:

    ```toml
    [hook]
    on-activate = '''
      mkdir foo
    '''
    ```

=== "Containers"

    This would be performed with another `RUN` command,
    though it creates another layer in the image:

    ```dockerfile
    RUN mkdir foo
    ```

---

## Share the environment with your team

Suppose you work on a team and you've just set up the development environment.
Now you want to share it with your team so you can ensure that everyone has the
same environment.

=== "Flox"

    Since [`flox init`][init] creates a `.flox` directory inside your project,
    you can simply check this directory into source control.

    ```console
    $ git add .flox
    $ git commit -m "Add Flox environment"
    $ git push
    ```

    Anyone with Flox installed can now work on this project with two commands:

    ```console
    $ git clone <your repo>
    $ flox activate
    ```

    Any packages not locally cached would be downloaded.
    Since the Flox environment produces a lockfile each time it is built,
    every developer that does a [`flox activate`][activate] with the same
    lockfile will get the same exact software down to the `git` revisions of the
    upstream source repositories.

    If your environment doesn't need to be tied to this specific project you
    could also push the environment to FloxHub with [`flox push`][push].
    Then your team would activate the environment as a "remote" environment:

    ```console
    $ # You
    $ flox push
    $ # Your coworker
    $ flox activate -r your_user/myproject
    ```

=== "Containers"

    The `Dockerfile` would be checked into source control,
    then each developer would build the image locally via `docker build`.
    However, since _building_ the image isn't reproducible
    (packages in the repositories may have new updates/bugs, base image may
    have been updated),
    each developer may have a slightly different development environment.

    It's possible to ensure that all of the developers get the same software
    by building the image in a CI system and having developers avoid building
    the image locally.

    - Create a repository or CI rule that builds the development image every
      time the `Dockerfile` changes.
    - Build the image in CI and upload the image to a registry.
    - Developers `docker pull` the image when there are updates.

    This is additional complexity though, and requires extra infrastructure.

---

## Development-time services

In order to mimic the production environment you may want some services running
during development (e.g. a web server, a database, etc).

For this example let's say you want a minimal Caddy server running with some
environment variables set.

=== "Flox"

    First install Caddy:

    ```{ .bash .copy }
    flox install caddy
    ```

    Then [edit][edit] your manifest to create a new [service][services]:

    ```toml
    [services.server]
    command = "caddy run"
    vars.VAR1 = "var1"
    vars.VAR2 = "var2"
    ```

    Since Flox environments aren't isolated from the host machine's network
    you don't need to map any ports.

    You can start this service from inside the environment with
    [`flox services start`][services-start],
    or you can have it start automatically when entering the environment via
    `flox activate --start-services`.

=== "Containers"

    First create a `docker-compose.yml` file that pulls in a Caddy image:

    ```yaml
    version: "3.8"

    services:
      caddy:
        image: caddy:latest
        container_name: caddy_server
        ports:
          - "80:80"
          - "443:443"
        environment:
          - VAR1=var1
          - VAR2=var2
    ```

    This configuration maps the container's ports so that they're accessible
    from the host machine.

    The service is started separately via `docker-compose up`,
    but you may also add the development container to the `docker-compose.yml`
    file so that it's started at the same time as the server.

---

## Run tests in CI

Say you've done some development and now want to run your changes through CI.

=== "Flox"

    A CI system would activate the Flox environment for the repository and then
    run a specified command inside the environment for each step of the CI job.

    Since a Flox environment contains a lockfile,
    a CI system that runs `flox activate` will get exactly the same software
    as the developer pushing the changes.
    This greatly reduces the number of "it works on my machine" instances.

    Flox provides a number of plugins for CI providers,
    including Github Actions, CircleCI, and GitLab.
    See the [CI/CD tutorial][ci-cd] for more information.

=== "Containers"

    A CI system would either pull the development image from a registry or
    build it if necessary.
    The CI system would then run a specified command inside the container for
    each step in the CI job.

---

## Send artifacts to production

Now that you have a working development environment,
you need to build a container so that it can be deployed.

=== "Flox"

    You can create a container from an environment via the
    [`flox containerize`][containerize] command,
    and this image will contain the same exact software
    (again, down to the `git` revisions of the upstream source repositories)
    that you used for both local development and CI.
    If your environment already contains the programs you want to run in
    production, you're in good shape.

    There is a work in progress feature for producing build artifacts from
    a Flox environment.
    We have some exciting things happening in this space!
    If you're interested in early access for this feature,
    see our [early access page][early].

=== "Containers"

    Typically your `Dockerfile` will contain multiple stages,
    possibly a base `builder` stage, a development stage that builds on
    `builder`, and a production stage that contains only the executable.

    You would typically build this image in CI via a `docker build` command
    that targets the production stage.
    CI would also upload the production image to a container registry.

---

[init]: ../man/flox-init.md
[edit]: ../man/flox-edit.md
[install]: ../man/flox-install.md
[push]: ../man/flox-push.md
[containerize]: ../man/flox-containerize.md
[activate]: ../man/flox-activate.md
[services-start]: ../man/flox-services-start.md
[services]: ../concepts/services.md
[manifest]: ../concepts/environments.md#manifesttoml
[early]: https://flox.dev/early/
[ci-cd]: ../tutorials/ci-cd.md

---


## What is FloxHub?

> Source: `concepts/floxhub.md`

---
title: What is FloxHub?
description: Everything you need to know about FloxHub.
---

# What is FloxHub?

FloxHub is a cloud service that enables you to share your Flox
[environments][environments_concept].

## Account creation in FloxHub

When signing up for a FloxHub account,
we will **automatically use your GitHub username as the FloxHub account name**.

When you [`flox push`][flox_push] an environment to FloxHub,
you will be prompted to create an account.
You can return to FloxHub to view your environments any time at
[hub.flox.dev](https://hub.flox.dev).

    If you need to share environments with a team, you can create an [Organization][organizations_concept] and push environments there instead of your personal account.

### Authenticating with the CLI

You can authenticate with FloxHub from the Flox CLI.
Run [`flox auth login`][flox_auth] and follow the on-screen instructions.

## Working with Environments in FloxHub

### Environment page

The FloxHub Environment page allows you to **browse all the
[environments][environments_concept] you have shared** with
[`flox push`][flox_push].

You can also:

* **Search** for environments by name.
* **Filter** for compatible system types.

Once you have found an environment that interests you,
you can:

* Open the **Environment Details** page for the selected environment by
**clicking on the environment name**.
* Use the **Share button** to copy CLI sharing commands pre-populated with the
environment name.
* Use the **Delete button** to delete the environment from FloxHub.
* Use the **Generations shortcut button** to jump into the generations tab of
the Environment Detail page.

### Environment Detail page

The FloxHub Environment Detail page lets you verify the contents of your
environment and view its history in FloxHub.

* **Sidebar**: shows key facts about the environment's live generation, like
the systems supported and the last modified date.
Below the key facts is a shortcut to the CLI sharing commands.
* **Details tab**: shows you packages that are in your
[environment's manifest][manifest_concept].
If your package was installed with a semantic version requirement,
that information will show on the right side.
* **Generation tab**: shows you the history of your environment through each
[generation][generation_concept].
Each new [`flox push`][flox_push] creates a new generation.
* **History tab**: describes the updates between each generation.
Packages that were installed with [`flox install`][flox_install] and uninstalled
with [`flox uninstall`][flox_uninstall] will be explicitly marked.
Packages that were added manually in a text editor or with
[`flox edit`][flox_edit] will show as "Manually edited".
* **Settings tab**: displays key information about your environment, like the
owner and its name.

### Automated upgrades

--8<-- "paid-feature.md"

To avoid missing important updates to your packages, it's a best practice to regularly upgrade your environments.
You can do this manually using the [`flox upgrade`][flox_upgrade] command or by clicking **Upgrade now** on the environment detail page in FloxHub.
However, if you have an [Organization][organizations_concept], you can let FloxHub upgrade your environments automatically.

#### Configure environment upgrades

Automated upgrades are enabled by default for all environments in an organization.
To change the default setting for an individual environment:

1. Sign in to [FloxHub][floxhub]
2. Choose an environment in an organization for which you're a *writer* or *owner*
3. Open that environment's detail page
4. Go to **Settings** > **Automated Upgrades**
5. Change the upgrade cadence to **Daily**


#### Organization-wide upgrade policy

You may choose to opt-out of automated upgrades for new environments, or turn them off for all environments in an organization.
To change your organization's upgrade policy:

1. Sign in to [FloxHub][floxhub]
2. Go to the detail page for an organization for which you're an *owner*
3. Go to **Settings** > **Automated Upgrades**
4. Select **Enable for new environments** to automatically upgrade new environments every day.
5. Select **Pause for all environments** to disable automated upgrades for all environments in this organization.


## Referring to FloxHub environments

When referring to FloxHub environments in the CLI,
you'll refer to the environment owner's account name, a forward slash `/`,
and the environment name.
Many commands use this syntax with the `-r` flag (which operates on your local copy),
and some commands such as [`flox pull`][flox_pull] that implicitly refer to
an environment on FloxHub.
See the [FloxHub environments][floxhub_environments] concept page for more details on how local and upstream copies work.

```{ .sh .copy }
flox pull example-owner/example-env
```

## Logging out of FloxHub

### Logging out in the web application

* Select the **portrait in the upper-right corner** of the screen
* Select **Log out** in the menu

### Logging out in the CLI

Run the [`flox auth logout`][flox_auth] command.

[flox_website]: https://flox.dev
[flox_push]: ../man/flox-push.md
[flox_pull]: ../man/flox-pull.md
[flox_activate]: ../man/flox-activate.md
[flox_auth]: ../man/flox-auth.md
[flox_edit]: ../man/flox-edit.md
[flox_install]: ../man/flox-install.md
[flox_uninstall]: ../man/flox-uninstall.md
[flox_upgrade]: ../man/flox-upgrade.md
[generation_concept]: ../concepts/generations.md
[manifest_concept]: ../concepts/environments.md#manifesttoml
[environments_concept]: ../concepts/environments.md
[organizations_concept]: ../concepts/organizations.md
[floxhub]: https://hub.flox.dev
[floxhub_environments]: ./floxhub-environments.md

---


## What is a generation?

> Source: `concepts/generations.md`

---
title: What is a generation?
description: Everything you need to know about generations.
---

# What is a generation?

Generations refer to a **version number of an environment** on
[FloxHub][floxhub_concept].
Both imperative and declarative commands that modify an environment on
FloxHub increment the generation number for the environment.

Read more about creating your first generation in the
[sharing guide][sharing_guide].

## First generation

The first environment generation (1) is created when you use
**[`flox push`][flox_push]** to send an environment to
[FloxHub][floxhub_concept].

## New generations

**New generations are created automatically** when you use a CLI command that
modifies the environment,
such as [`flox install`][flox_install] or [`flox edit`][flox_edit].

## Staged local generations

With a [FloxHub environment][environment_guide] **new local
generations are staged automatically**,
whether you pull into a directory or use `--reference`.
Suppose you [`flox pull`][flox_pull] an environment at generation 15 on
[FloxHub][floxhub_concept].
If you now run [`flox install`][flox_install] three times then you will have
generations 16-18 locally.
The next [`flox push`][flox_push] would sync these three new generations to
FloxHub if you have permission to write to the environment.

## Switching and viewing generations

Generations offer change management for environments;
it's similar to `git`, but tailored for environments.

Suppose you make an edit to an environment,
but then after activating and using the environment, you want to undo the change
you just made.
To undo the change, you can run `flox generations rollback`.

If you've made a series of edits over time but later realize you want to discard them all,
you can use `flox generations list` to display all the different versions of the environment, and then you can use `flox generations switch <generation number>`
to revert to the version of the environment prior to all the environments.
You can also view generations on FloxHub on the `Generations` tab of an
environment's page.

## History

Rolling back to a previous generation introduces another concept:
history.
Rolling back doesn't create a new generation, but it does add an entry to the environment's history.
Suppose you `flox generations rollback` from generation 18 to 17.
Although the list of generations hasn't changed, the latest entry in the environment's history will now say that generation 17 is the live generation.
Note that although generation 18 is the "latest" in the sense that it has the
highest generation number and was most recently created, it is not the latest to
be live.

This history of what generation is live at a given point in time can be
viewed on FloxHub on the `History` tab for an environment.
Or, to use the CLI to view history, you can run `flox generations history`.
This provides a log of what generation of an environment was live at the time
an environment was pulled.

## Generation lock

[FloxHub environments][environment_guide] that are pulled with
[`flox pull`][flox_pull] will store a generation lock which describes
**the current pulled generation**.
This allows this environment to advance to newer generations explicitly on the
next [`flox pull`][flox_pull].

[floxhub_concept]: .//floxhub.md
[flox_push]: ../man/flox-push.md
[flox_install]: ../man/flox-install.md
[flox_edit]: ../man/flox-edit.md
[flox_pull]: ../man/flox-pull.md
[sharing_guide]: ../tutorials/sharing-environments.md
[environment_guide]: ../tutorials/creating-environments.md

---


## Gitlab Ci

> Source: `k8s/examples/gitlab-ci.md`

---
title: "GitLab CI"
description: "Demo running GitLab CI with Imageless Kubernetes"
---

You can use Imageless Kubernetes in many applications where you would rely on a conventional image-based workflow.

This example shows how you can use Imageless Kubernetes with GitLab CI, running jobs inside of the same Flox environment you use for development.

## GitLab runner configuration

To configure your GitLab runner to run Imageless Kubernetes pods, add this section to the runner's `config.toml`:

```toml
[[runners]]
  [runners.kubernetes]
    namespace = {% raw %}"{{ default .Release.Namespace .Values.runners.jobNamespace }}"{% endraw %}
    runtime_class_name = "flox"
    image = "flox/empty:1.0.0"
    pod_annotations_overwrite_allowed = '^flox\.dev.*'
    [runners.kubernetes.pod_annotations]
      "flox.dev/skip-containers" = "init-permissions,helper"
      "flox.dev/skip-containers-exec" = "build"
      "flox.dev/activate-mode" = "dev" # optional
```

    These options can also be passed as part of the job definition in `.gitlab-ci.yml`, see the [GitLab documentation][gitlab-k8s-docs] for more details.

These settings will start all GitLab job pods using the Flox runtime, with an empty container image, and allow setting additional annotations (e.g. `flox.dev/environment`) on a per-job basis.

The `flox.dev/skip-containers` and `flox.dev/skip-containers-exec` annotations are necessary to allow GitLab's init containers to get the code and job script into build container for execution.

`flox.dev/activate-mode` is set to make build dependencies available to the job script.

See the [configuration][config] page for more details on annotations.

## GitLab job configuration

Once you've configured the runner, you will need to supply each job with the desired `flox.dev/environment` annotation, which can be done in `.gitlab-ci.yml`:

```yaml
stages:
  - hello

hello-job:
  stage: hello
  variables:
    KUBERNETES_POD_ANNOTATIONS_1: "flox.dev/environment=flox/hello"
  script:
    - hello
```

where the value of the annotation is the name of an environment from [FloxHub][floxhub].

    The `flox.dev/environment` annotation is *not* optional -- pods will fail to start if it is not supplied.

## Conclusion

Now, any job you target to this runner will be executed with Imageless Kubernetes.

If you utilize the same Flox environment used for development, you will be able to seamlessly test with the exact same packages, regardless of what system or architecture is used.

Since the CI environment doesn’t rely on a container image, updates are instant: run `flox push`, and the job will pick up the changes automatically.

[gitlab-k8s-docs]: https://docs.gitlab.com/runner/executors/kubernetes/
[config]: ../config.md
[floxhub]: ../../concepts/floxhub.md

---


## Go

> Source: `languages/go.md`

---
title: Go
description: Common questions and solutions for using Go with Flox
---

# Go

## Build with Flox

Not only can you _develop_ your software with Flox, but you can _build_ it as well.
See the [builds][build-concept] concept page for more details.

### Manifest builds

Since the output of the build must be copied to the `$out` directory, you may either install the output directly to `$out`, or you may copy the executable there manually after running `go build`.

Install directly to `$out`:

```toml
[build.myproject]
command = '''
  GOBIN=$out/bin go install -trimpath
'''
```

Copy the executable manually:

```toml
[build.myproject]
command = '''
  mkdir -p $out/bin
  go build -trimpath
  cp ./myproject $out/bin/myproject
'''
```

#### Go compiler adds metadata

Go adds metadata to compiled binaries that allows details from the build environment to leak through.
For example, a compiled binary will contain absolute paths to source files.
This can cause builds to fail as it interferes with Flox's ability to determine when a build depends on an artifact that aren't included in the build's closure, i.e. when a build has missing dependencies.
To address this you'll need to compile your programs with the `-trimpath` option.

#### Go builds depend on iana, mailcap, tzdata

The Go `net/http` package has a few runtime dependencies that you may not know you depend on:

- `iana-etc`: used to resolve a protocol or service by name.
- `mailcap`: used to resolve MIME types.
- `tzdata`: used to resolve timezones.

You'll need to add those packages to your environment

```toml
[install]
iana-etc.pkg-path = "iana-etc"
mailcap.pkg-path = "mailcap"
tzdata.pkg-path = "tzdata"
```

and add them to the `runtime-packages` of your build if you're limiting which packages are present at runtime:

```toml
runtime-packages = [
  "iana-etc",
  "mailcap",
  "tzdata",
]
```

#### Vendoring dependencies in pure builds

As discussed in the [pure builds][pure-builds-section] of the Builds concept page, pure builds run in a sandbox without network access on Linux.
A pure build can be run as a multi-stage build where the first step vendors dependencies.
An example is shown below:

```toml
[build.myproject-deps]
command = '''
  export GOMODCACHE=$out
  go mod download -modcacherw
'''

[build.myproject]
command = """
  export GOMODCACHE=${myproject-deps}
  mkdir -p "$out/bin"
  go build -trimpath -o $out/bin/myproject
  chmod +x $out/bin/myproject
"""
sandbox = "pure"
```

### Nix expression builds

To build a project using [`buildGoModule`](https://nixos.org/manual/nixpkgs/stable/#sec-language-go) which will import your existing dependency file, but you will need to [update the hash][nix-expression-hashes]:

```go
{ buildGoModule }:

buildGoModule {
  pname = "myproject";
  version = "0.1.0";
  src = ../../../.;

  vendorHash = "<YOUR_HASH>";
}
```

[build-concept]: ../concepts/builds.md
[pure-builds-section]: ../concepts/manifest-builds.md#pure-builds
[nix-expression-hashes]: ../concepts/nix-expression-builds.md#generating-hashes

---


## Homebrew migration guide

> Source: `tutorials/migrations/homebrew.md`

---
title: Homebrew
description: Using Flox to replace or augment Homebrew
---

# Homebrew migration guide

Flox is an environment and package manager all in one. Using Flox, you can create discrete environments containing packages from the Flox Catalog.

Flox can replace [Homebrew](https://brew.sh) entirely, or they can be used together.

This guide explains how to introduce Flox into environments where Homebrew is currently being used, either as a replacement or an addition. It introduces new concepts and proposes a basic procedure for mapping packages.

## Why you might want to migrate

Homebrew does a great job, and has been loved as the “missing package manager” for a generation of macOS users. But there are a few reasons you might consider moving to Flox:

* **You need a cross-platform package manager.** Flox works on both macOS and Linux - x86 and ARM - allowing you to define a set of packages that works the same everywhere.
* **You need a virtual package manager** Flox allows you to create as many environments as you need, each with a different set of packages.
* **You need reproducible environments.** Flox environments are defined in a TOML [manifest][manifest_concept] that can be easily shared, or managed alongside code.
* **You need a broader set of software.** Homebrew has a sizeable collection of packages, but the Flox Catalog is based on Nixpkgs, the largest collection of packages in the world.
* **You need older versions of software.** The Flox Catalog contains historical versions of each of its packages, and makes it easy to install them.

## Install Flox

Download and install Flox following the [installation instructions][install_flox].

## Migrate your first package

Migrating to Flox is a straightforward process of installing Flox packages for each of your Homebrew formulae. This section walks you through the process for identifying the set of Homebrew formulae you currently have installed, searching for the corresponding packages in the Flox Catalog, and installing them.

As a Homebrew user, you will find several of the Flox subcommands familiar:

* [`search`][search] is used to find available packages
* [`install`][install] is used to install packages
* [`uninstall`][uninstall] is used to remove packages

### Show top-level formulae in Homebrew

First, identify the list of Homebrew packages you have installed.

We recommend using `brew leaves` for this, so you can easily differentiate between the formulae you installed explicitly versus those that were installed as dependencies. The `leaves` subcommand will show the formulae that were directly installed.

For example:

```console
% brew leaves
aider
awscli
ffmpeg
flake8
gh
gnupg
go
graphviz
htop
isort
jq
neovim
pkgconf
redo
ripgrep
tmux
tree
watch
wget
```

### Search for a package in Flox

Then, search Flox for one of the formulae you have installed with Homebrew. In this case, for example, you could choose `jq`:

```console
% flox search jq
jq                   Lightweight and flexible command-line JSON processor
ijq                  Interactive wrapper for jq
jql                  JSON Query Language CLI tool built with Rust
jqp                  TUI playground to experiment with jq
gojq                 Pure Go implementation of jq
jq-lsp               jq language server
jquake               Real-time earthquake map of Japan
jq-zsh-plugin        Interactively build jq expressions in Zsh
vimPlugins.jq-vim    <no description provided>
python37Packages.jq  Python bindings for jq, the flexible JSON processor

Showing 10 of 80 results. Use `flox search jq --all` to see the full list.

Use 'flox show <package>' to see available versions
```

The first one on the list is the correct Flox package to install, and it has the same name as the Homebrew package. This will often be the case, but not always.

### Install your first package

To install your first package, use `flox install`:

```{ .sh .copy }
flox install jq
```

The first time you install a package, Flox will ask you whether you want to create a [default environment][default_tutorial].

```console
% flox install jq
Packages must be installed into a Flox environment.
A default environment on FloxHub will sync across all your machines.

! Would you like to pull or create your 'default' environment and install 'jq' to it?
> Yes
  No
[↑↓ to move, enter to select, type to filter]
```

If you choose to do so, Flox will then ask you whether you want to configure your shell to automatically activate the new default environment.

```console
The 'default' environment can be activated automatically for every new shell
by adding one line to your .bashrc and .profile files:
eval "$(flox activate -r <user>/default -m run)"

! Would you like Flox to add this configuration to .bashrc and .profile now?
  Yes
> No
[↑↓ to move, enter to select, type to filter]

✅ Configuration added to your .bashrc file.
The 'default' environment will be activated for every new shell.
-> Restart your shell to continue using the default environment.
-> Read more about the 'default' environment at:
   https://flox.dev/docs/tutorials/layering-multiple-environments/#create-your-default-home-environment

✅ 'jq' installed to environment '<owner>/default' (local)
```

When Flox is configured with a default environment, it behaves very similarly to Homebrew. The Flox CLI will assume the default environment when you run `flox install` in a directory that doesn't contain an environment of its own.

Creating a Flox default environment is optional.

If you do not choose for this to be automated at the time of your first package installation, or you want to use an existing environment on FloxHub, you can [follow these instructions][default_tutorial_setup] to add Flox to your dotfiles manually.

### Verify configuration

Exit your active shell and create a new one, causing the dotfile changes to take effect. The first time this happens, you may experience a delay while your default environment is materialized. The next time you open a shell it should be quick because the environment has been cached.

Once the shell is available, you can verify that your default environment is active by running [`flox envs`][envs]:

```console
flox [default] % flox envs
✨ Active environments:
  default           https://hub.flox.dev/user/default
```

If you see `default` listed amongst the active environments, your dotfiles have been correctly modified. The default environment will be active whenever you log in.

Verify that your package has been installed using [`flox list`][list]:

```console
flox [default] % flox list
jq: jq (1.7.1)
```

## Create environments for projects

As you continue to migrate packages from Homebrew to Flox, you may find that you don’t need them all in your default environment.

The default environment is intended for packages that should be available to the user across all of the contexts where they work. It is commonly used for general utilities like `gh`, `gnused`, and `curl` that apply to many situations.

Packages that are required for specific contexts (e.g., different projects in a monorepo, different repos, different customer deployments, etc.) are often installed into path environments which are then activated in addition to the default environment.

That means there are a few additional subcommands to learn when using Flox:

* `init` creates a new environment
* `activate` activates an environment, to make the packages available

View the [creating environments][creating_tutorial] page for more details.

When installing packages that you are accustomed to getting from Homebrew, consider the following guidelines:

* install the packages you always need into your default environment, and
* install the rest into environments for the projects or contexts where they are required.

## Complete the migration

Once you have installed all of the Flox packages you need, you have a few options. You can either uninstall Homebrew and use Flox exclusively, or you can use them together.

### Option 1: Uninstall Homebrew

If Flox has everything you need and is working satisfactorally, you may no longer need Homebrew. In this case, it’s a good idea to uninstall it so it doesn’t affect your system in potentially confusing ways.

To do this, follow [the instructions in the Homebrew FAQ](https://docs.brew.sh/FAQ#how-do-i-uninstall-homebrew).

### Option 2: Use Flox and Homebrew together

Homebrew and Flox can be used together, and there is no need to uninstall Homebrew in order to use Flox.

However, if you have the Flox default environment enabled, you should be aware of the order of Homebrew and Flox entries in your dotfiles. Both Homebrew and Flox modify your `PATH`, and the one that appears later in your dotfiles will take precedence. If the same package is installed using both Homebrew and Flox, this order will become important.

We recommend that the Flox default environment activation lines appear lowest in your dotfiles, ensuring that packages in the default environment appear in your `PATH` sooner than those from Homebrew.

[manifest_concept]: ../../concepts/environments.md#manifesttoml
[default_tutorial]: ../default-environment.md
[default_tutorial_setup]: ../default-environment.md#initial-setup
[creating_tutorial]: ../creating-environments.md
[install_flox]: ../../install-flox/install.md
[search]: ../../man/flox-search.md
[envs]: ../../man/flox-envs.md
[list]: ../../man/flox-list.md
[catalog]: ../../concepts/packages-and-catalog.md
[install]: ../../man/flox-install.md
[uninstall]: ../../man/flox-uninstall.md
[activate]: ../../man/flox-activate.md

---


## Intro

> Source: `k8s/intro.md`

---
title: "Introduction"
description: "What is Imageless Kubernetes?"
---

Imageless Kubernetes is a new way to run Kubernetes backed by Flox environments rather than container images.
This means that rather than managing image pipelines and constantly rebuilding containers, you now have lightweight Flox environments that *build reproducibly*, with centralized control via FloxHub.
And since Flox environments give you the same set of dependencies no matter where they're run, you can rest easy knowing that the tools you used during development and CI are the same as those running in a Kubernetes pod.

Let's take a closer look at what this buys you.

## Centralized management

Each pod specifies a command to run and the Flox environment to run inside of it.
The syntax is slightly different to a typical pod spec, so the syntax will be explained shortly.
For now, just know that you need to specify a Flox environment to run your command in.

The environment you specify must be an environment that has been pushed to FloxHub because this is where the centralized management magic happens.
Once the environment has been pushed to FloxHub, you get:

- A list of the installed packages and their versions
- A list of the environment variables set by the environment
- The scripts that run on startup
- An audit trail of what changes were made to the environment and by whom

Once an environment has been pushed to FloxHub, FloxHub becomes the source of truth.

## Syntax

A sample pod specification is shown below:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: flox-containerd-demo
  annotations:
    # Required: the FloxHub environment to be activated within the pod
    flox.dev/environment: "flox/echoip"
    # Optional: disable Flox metrics reporting
    # flox.dev/disable-metrics: "false" # default
spec:
  # Required: directs containerd to use the Flox backend
  runtimeClassName: flox
  containers:
    - name: echoip
      # We provide `flox/empty` as a demonstration that the Flox
      # environment requires nothing from the container image.
      image: flox/empty:1.0.0
      # The command to run inside your environment
      command: ["echoip"]
```

In short, you specify the Flox environment as an annotation, then provide a command to run inside the environment via a command to a dummy container (`flox/empty:1.0.0`) that's only a few bytes in size.
As explained above, this workaround is required by Kubernetes pod specification.

## Workflow

Once you create a pod specification and deploy it, the pod will start up with the currently live [generation][generations-concept] of the environment.

Now let's say you want to add a package to the environment running in the pod.
All you need to do is install the package to the environment, and redeploy the pod.
No need to rebuild an image.

Here's what happens under the hood:

- An operator runs `flox install -r myorg/myenv somepackage`.
- This creates a new generation of the local copy of the environment.
- The operator then runs `flox push -r myorg/myenv` to sync the changes to FloxHub.
- Next time the pod is deployed, it will pull the latest generation from FloxHub (which now contains `somepackage`)

It's that simple.

## Trying it out

To quickly try out Imageless Kubernetes locally, see the [examples][examples-section], which uses `kind` to create a local Kubernetes cluster.

Imageless Kubernetes is also currently available for:

- Amazon EKS
- Self-managed Kubernetes

See the [installation][install-section] for more details on installing Imageless Kubernetes in your cluster.

[generations-concept]: ../concepts/generations.md
[install-section]: ./install/eks.md
[examples-section]: ./examples/kind-demo.md

---


## JVM

> Source: `languages/jvm.md`

---
title: JVM
description: Common questions and solutions for using the JVM ecosystem with Flox
---

# JVM

## Build with Flox

Not only can you _develop_ your software with Flox, but you can _build_ it as well.
See the [builds][build-concept] concept page for more details.

### Manifest builds

This example will use [Gradle][gradle] and the [shadowJar][shadow] plugin, though a number of build systems exist in the Java ecosystem.
The core of building a Java artifact with Flox looks like this:

- Bundle the application into a JAR
- Place the JAR into `$out/lib/`
- Create a script that calls `java -jar <path to jar>`, where `<path to jar>` is the path to the jar in `$out/lib` at runtime, where `$out` is not set.

```toml
[build.myproject]
  # Create the destination directories
  mkdir -p "$out"/{lib,bin}
  # Build a fat jar with gradle using the shadowJar plugin
  gradle shadowJar
  # Copy the newly built jars to $out
  cp build/libs/*.jar $out/lib

  # Build a script that gets the absolute path to the JAR at run time
  # and then calls 'java -jar $JAR_PATH'
  echo '#!/usr/bin/env bash' > $out/bin/myproject
  echo 'SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"' >> $out/bin/myproject
  echo 'JAR_PATH="$SCRIPT_DIR/../lib/myproject-app-all.jar"' >> $out/bin/myproject
  echo 'exec java -jar "$JAR_PATH" "$@"' >> $out/bin/myproject

  # Ensure that the script has the correct permissions
  chmod 755 $out/bin/myproject
```

Since `$out` is not set at runtime, the script that calls `java -jar <path to jar>` needs to find the location of the JAR at runtime.
Note that `pwd` will return the location from which the built artifact is run, not the location of the artifact itself, which is why the script goes through the process of setting `SCRIPT_DIR` and `JAR_PATH`.

[gradle]: https://gradle.org/
[shadow]: https://gradleup.com/shadow/
[build-concept]: ../concepts/builds.md

---


## K8S Shim Cli Version

> Source: `snippets/k8s-shim-cli-version.md`

## Versioning

The installation procedure described here will install the latest version of the Flox CLI and runtime shim that is available when the nodes are created.
Any time you replace a node, either of these may be updated to the latest version.

---


## Kind Demo

> Source: `k8s/examples/kind-demo.md`

---
title: "Web server with Redis"
description: "Demo running a simple web server backed by Redis on kind"
---

With Imageless Kubernetes, you can run a container just like in any other
Kubernetes deployment, but you don't have to build a container image.

To demonstrate this, we'll run a simple web server backed by Redis using two
Flox environments.

## Running the example

The entirety of this example can be run locally with the following commands:

```bash
git clone https://github.com/flox/flox-kind-demo.git
cd flox-kind-demo
flox activate
just up
```

This starts a local Kubernetes cluster using `kind` and deploys a web server
backed by Redis.

To fetch something from the web server, run:

```bash
curl localhost:3000/quotes/0
```

## Quotes app environment

The example runs a deployment of [`flox/quotes-app`](https://hub.flox.dev/flox/quotes-app), which is just like any other
Kubernetes deployment, but with a few key differences.
Here's a snippet from the deployment manifest:

```yaml
metadata:
  labels:
    app: quotes
  annotations:
    flox.dev/environment: "flox/quotes-app"
spec:
  runtimeClassName: flox
  containers:
    - name: quotes
      image: flox/empty:1.0.0
      command: ["quotes-app-go", "-r", "redis:6379"]
```

The full deployment manifest can be found in the
[flox-kind-demo repo](https://github.com/flox/flox-kind-demo/blob/main/quotes.yaml).

There are two key lines needed to run the container using a Flox environment
instead of a container image:

- Specifying `runtimeClassName: flox` runs the container using the Flox
  containerd shim.
- The annotation `flox.dev/environment: "flox/quotes-app"` specifies the Flox
  environment to use to bootstrap the container filesystem instead of a container image

Just as with any container, you can specify a startup command, which is
`["quotes-app-go", "-r", "redis:6379"]` in this case.

When the container starts, the [`flox/quotes-app`](https://hub.flox.dev/flox/quotes-app) Flox environment is pulled from FloxHub and bind mounted into the container.
This environment contains the [`flox/quotes-app-go`](https://hub.flox.dev/packages/flox/quotes-app-go) package, which is a simple web server published to FloxHub.
When the container starts, the environment is activated, and then `quotes-app-go` is run inside the activated environment.

### Redis environment

The `quotes-app-go` server uses a Redis instance running in a second deployment.
Just like the first pod, rather than specifying a container image, the Redis
deployment runs the environment `flox/redis` which is pulled from
[hub.flox.dev/flox/redis](https://hub.flox.dev/flox/redis).

Here's the relevant snippet from the Redis deployment manifest:

```yaml
metadata:
  labels:
    app: redis
  annotations:
    flox.dev/environment: "flox/redis"
spec:
  runtimeClassName: flox
  containers:
    - name: redis
      image: flox/empty:1.0.0
      command: ["redis-server", "--daemonize", "no", "--dir", "/data", "--bind", "0.0.0.0", "--protected-mode", "no" ]
      volumeMounts:
        - name: redis-data
          mountPath: /data
```

The full deployment manifest can be found in the
[flox-kind-demo repo](https://github.com/flox/flox-kind-demo/blob/main/redis.yaml).

## Updating the deployment

Because the environment is hosted on FloxHub, there's no need to rebuild a
container image to update the deployment.
After a change to `quotes-app-go`, updating the deployment would require running
a `flox publish` for `quotes-app-go` and a `flox upgrade -r flox/quotes-app`.
After that, restarting a pod will pull the latest generation of the environment.
This allows deploying software with the reproducibility of a container, but
without the overhead of having to rebuild an entire container image when iterating.

## Cleaning up

To tear down the local kind cluster, run:

```bash
just down
```

---


## Known issues

> Source: `customer/known-issues.md`

---
title: Known issues
description: Known issues
---

# Known issues

## Build

### False positive dependencies

Currently it's possible for false positive detection of missing dependencies.
For example, the Go compiler embeds metadata into compiled binaries, including the path to the compiler itself.
When scanning a Go-compiled binary for references to missing dependencies, Nix will detect a reference to the Go compiler and erroneously claim that your binary depends on the Go compiler.

The mitigation for this bug varies from language to language, but in this Go case the mitigation is as simple as using the `-trimpath` compilation flag.

It's also worth noting that sometimes what appears as a false positive missing dependency is actually a runtime dependency that you wouldn't know is missing until a certain codepath in your executable is triggered.
In short, ensure that you've done your due diligence to find out whether a missing dependency is actually a false positive.

---


## Nix Expression Builds

> Source: `concepts/nix-expression-builds.md`

---
title: "Nix expression builds"
description: Nix expression builds with Flox
---

See the [builds concept][builds-concept] page for an overview of the different types of builds and how to perform them.

## Overview

Nix expression builds are defined by creating files in the `.flox/pkgs/` directory of a Flox environment. These expressions are written in the Nix language, which is incredibly powerful and results in truly reproducible builds.

The environment that contains the builds doesn't need to have any packages installed because all of the build's dependencies are defined within the expression, but if there are any packages installed then Flox will attempt to produce a build that is compatible with any packages in the "toplevel" [package group][pkg-groups].

## Defining builds

Each build specified in the `.flox/pkgs/` directory corresponds to a different package with the name taken from a combination of the path and file names, for example:

| Path | Name |
| ---- | ---- |
| `.flox/pkgs/hello.nix` | `hello` |
| `.flox/pkgs/hello/default.nix` | `hello` |
| `.flox/pkgs/hello/how/do/you/do/default.nix` | `hello.how.do.you.do` |

These names cannot conflict with [manifest builds][manifest-builds-concept] in the same environment and will result in an error if they do.

All of the files in the `.flox/pkgs` directory must be tracked by a Git repository (`git add`ed but not necessarily committed) which ensures that unnecessary cache files and secrets don't end up in your package.

## What can you build?

Nix provides a variety of helpers for common builds and language frameworks to help you package your own software:

* [Language support](https://nixos.org/manual/nixpkgs/stable/#chap-language-support)
* [Trivial builders](https://nixos.org/manual/nixpkgs/stable/#chap-trivial-builders)

You can also make modifications to existing packages that are already in the Flox Catalog.

### Example: Distributing a script

To distribute a simple shell script which has a dependency on existing packages:

```{ .nix .copy title=".flox/pkgs/my-ip.nix" }
{writeShellApplication, curl}:

writeShellApplication {
  name = "my-ip";
  runtimeInputs = [ curl ];
  text = ''
    curl icanhazip.com
  '';
}
```

This will ensure that a known version of `bash` and `curl` are available to the package at runtime. It will also automatically add some error handling options (`errexit`, `nounset`, `pipefail`) and validate the script with `shellcheck`.

### Example: Building your own project

To build a Rust project that lives in the same repository as your Flox environment:

```{ .nix .copy title=".flox/pkgs/quotes-app-rust.nix" }
{ rustPlatform, lib }:

rustPlatform.buildRustPackage rec {
  pname = "quotes-app-rust";
  version = "0.1.0";

  src = ../../.;
  cargoLock.lockFile = "${src}/Cargo.lock";

  meta = with lib; {
    description = "Quotes App written in Rust";
    license = licenses.mit;
  };
}
```

This will vendor dependencies from your `Cargo.lock` file, run `cargo build`, and package the resulting binary.

### Example: Building a third-party project

If there's an open source Go project that isn't already available in the Flox Catalog:

```{ .nix .copy title=".flox/pkgs/quotes-app-go.nix" }
{ buildGoModule, fetchFromGitHub, lib }:

buildGoModule rec {
  pname = "quotes-app-go";
  version = "0.1.0";

  src = fetchFromGitHub {
    owner = "flox";
    repo = "flox-manifest-build-examples";
    rev = "285aaa8334762f2006151b03208a51527ff762e9";
    hash = "sha256-4BACKTYqsq0ZHno1jXCta4761pv3rFhlSEpVRWltSqQ=";
  };
  sourceRoot = "${src.name}/${pname}";
  vendorHash = "sha256-8wYERVt3PIsKkarkwPu8Zy/Sdx43P6g2lz2xRfvTZ2E=";

  meta = with lib; {
    description = "Quotes App written in Go";
    license = licenses.mit;
  };
}
```

This will vendor dependencies from your `go.mod` file, run `go build`, and package the resulting binary.

### Example: Extensions of an existing package

If you want to use VS Code with some pre-installed extensions:

```{ .nix .copy title=".flox/pkgs/vscode-with-extensions.nix" }
{vscode, vscode-utils, vscode-extensions, vscode-with-extensions}:

vscode-with-extensions.override {
  inherit vscode;

  vscodeExtensions = with vscode-extensions; [
    bbenoist.nix
    github.copilot
  ] ++ vscode-utils.extensionsFromVscodeMarketplace [
    {
      name = "flox";
      publisher = "flox";
      version = "0.0.2";
      hash = "sha256-wvRhPPSnCimpB1HEbAg7a0r9hFKzMZ/Z1vS+XVmviOM=";
    }
  ];
}
```

This will add the Nix, GitHub Copilot, and Flox extensions to the VS Code package.

### Example: Newer version of an existing package

If the latest version of a package isn't yet available in the Flox Catalog then you can often just override the `version` and `src` attributes of the existing package:

```{ .nix .copy title=".flox/pkgs/hello.nix" }
{ hello, fetchurl }:

hello.overrideAttrs (finalAttrs: _oldAttrs: {
  version = "2.12.2";
  src = fetchurl {
    url = "mirror://gnu/hello/hello-${finalAttrs.version}.tar.gz";
    hash = "sha256-WpqZbcKSzCTc9BHO6H6S9qrluNE72caBm0x6nc4IGKs=";
  };
})
```

### Example: Patches to an existing package

If you want to apply a patch, such as an unreleased bug fix, to an existing package:

```{ .nix .copy title=".flox/pkgs/hello-shouty/default.nix" }
{ hello }:

hello.overrideAttrs (oldAttrs: {
  patches = (oldAttrs.patches or []) ++ [
    ./shouty.patch
  ];
  meta = oldAttrs.meta // {
    description = "A patched version of hello that shouts the default greeting.";
  };
})
```

Note that this expression is saved as `default.nix` in its own sub-directory so that we can version control the patch as a separate file.
This build also defines tests so they have to be modified too:

```diff title="./flox/pkgs/hello-shouty/shouty.patch"
--- hello-2.12.2/src/hello.c  2025-05-19  12:49:04
+++ hello-patched/src/hello.c 2025-07-04 10:33:57
@@ -145,7 +145,7 @@
 #endif

   /* Having initialized gettext, get the default message. */
-  greeting_msg = _("Hello, world!");
+  greeting_msg = _("HELLO, WORLD!");

   /* Even exiting has subtleties.  On exit, if any writes failed, change
      the exit status.  The /dev/full device on GNU/Linux can be used for
diff -ru hello-2.12.2/tests/hello-1 hello-patched/tests/hello-1
--- hello-2.12.2/tests/hello-1  2025-05-19 12:49:04
+++ hello-patched/tests/hello-1 2025-07-04 10:48:38
@@ -21,7 +21,7 @@

 tmpfiles="hello-test1.ok"
 cat <<EOF > hello-test1.ok
-Hello, world!
+HELLO, WORLD!
 EOF

 tmpfiles="$tmpfiles hello-test1.out"
```

### Example: Vendor an existing package

Typically you would only override specific attributes of an existing package, which allows you to continue benefiting from upstream changes and surface failures if there are any conflicts, but if you want to copy a package to make more fundamental changes or because it's being removed upstream:

```{ .sh .copy }
mkdir -p .flox/pkgs
EDITOR=cat \
  nix --extra-experimental-features "nix-command flakes" \
  edit 'nixpkgs#hello' \
  > .flox/pkgs/hello.nix
```

This will extract the expression for the `hello` package in `nixpkgs` and save the contents to file which can then be modified.

## Tips

### Generating hashes

Expressions that fetch external dependencies will often specify hashes to ensure that they are reproducible, trusted, and speed up cached steps. The hash should be changed whenever you change a `src` or `url` otherwise the sources may not be fetched again or they will fail the validation check.

If you don't have a way of verifying the current hash and you trust the source then you can specify an empty string value:

```{ .nix .copy }
  src = fetchurl {
    url = "mirror://gnu/hello/hello-${finalAttrs.version}.tar.gz";
    hash = "";
  };
```

Then perform a `flox build` and take the correct value from the error message:

```console
warning: found empty hash, assuming 'sha256-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='
Building hello-2.12.2 in Nix expression mode
these 2 derivations will be built:
  /nix/store/srm7s6pyckifs52ikyfasf6bqkk2c5ls-hello-2.12.2.tar.gz.drv
  /nix/store/3d9n2f5pg2s4y3p46awmsp46fxpdfkg6-hello-2.12.2.drv
building '/nix/store/srm7s6pyckifs52ikyfasf6bqkk2c5ls-hello-2.12.2.tar.gz.drv'...
hello>
hello> trying https://ftpmirror.gnu.org/hello/hello-2.12.2.tar.gz
hello>   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
hello>                                  Dload  Upload   Total   Spent    Left  Speed
hello>   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
hello> 100 1141k  100 1141k    0     0   906k      0  0:00:01  0:00:01 --:--:-- 2218k
error: hash mismatch in fixed-output derivation '/nix/store/srm7s6pyckifs52ikyfasf6bqkk2c5ls-hello-2.12.2.tar.gz.drv':
         specified: sha256-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=
            got:    sha256-WpqZbcKSzCTc9BHO6H6S9qrluNE72caBm0x6nc4IGKs=
```

[builds-concept]: ./builds.md
[manifest-builds-concept]: ./manifest-builds.md
[pkg-groups]: ../man/manifest.toml.md#package-descriptors

---


## Node.js

> Source: `languages/nodejs.md`

---
title: Node.js
description: Common questions and solutions for using Node.js with Flox
---

# Node.js

## Build with Flox

Not only can you _develop_ your software with Flox, but you can _build_ it as well.
See the [builds][build-concept] concept page for more details.

### Manifest builds

#### npm

Building Node.js packages with `npm` looks similar to building for containers or serverless functions.
On a high level, builds for Node.js-based projects generally follow this pattern:

```toml
[build.myproject]
command = '''
# Install dependencies
npm ci

# Build
npm run build
# -> assuming this yields a `dist` directory

# Install the build result to `out` # (1)!
mkdir -p $out
mv ./dist $out/

## If your app does not use a bundler
## and needs additional node_modules at runtime,
## `npm prune` and copy the node modules to $out
#
# npm prune --include "prod"
# cp -r ./node_modules $out

# Create a run script # (2)!
mkdir -p $out/bin
echo "#!/usr/bin/env sh"
echo 'exec node $out/dist/index.js "$@"' >> $out/bin/myproject
chmod 755 $out/bin/myproject
'''
```

1. If you expect to install multiple Node.js applications in the same environment, we recommend putting the `dist` (and optional `node_modules`) under an appropriate namespace, e.g. install them as `/libexec/myproject/dist`.

2. If your `npm build` already produces a binary that can be executed drectly, you can also copy or link that to `$out/bin`. Note that only binaries in `$out/bin` are wrapped to ensure they run within a consistent environment.

#### Vendoring dependencies in pure builds

As discussed in the [pure builds][pure-builds-section] of the Builds concept page, pure builds run in a sandbox without network access on Linux.
A pure build can be run as a multi-stage build where the first step vendors dependencies.
An example is shown below:

```toml
[build.myproject-deps]
command = '''
  mkdir -p $out
  npm ci
  cp -r node_modules $out
'''

[build.myproject]
command = '''
  # Copy node modules built in the previous step
  cp --no-preserve=mode -r ${myproject-deps}/node_modules ./
  ...
  # The rest of the build is the same
'''
sandbox = "pure"
```

### Nix expression builds

To build a project using [`buildNpmPackage`](https://nixos.org/manual/nixpkgs/stable/#language-javascript) which will import your existing dependency file:

```nix
{
  buildNpmPackage,
  importNpmLock,
}:

buildNpmPackage (final: {
  pname = "myproject";
  version = "0.1.0";
  src = ../../../.;

  npmDeps = importNpmLock {
    npmRoot = final.src;
  };
  npmConfigHook = importNpmLock.npmConfigHook;
  npmBuildScript = "build";
});
```

[build-concept]: ../concepts/builds.md
[pure-builds-section]: ../concepts/manifest-builds.md#pure-builds

---


## Node Version Manager (nvm) migration guide

> Source: `tutorials/migrations/nvm.md`

---
title: Node Version Manager (nvm)
description: Using Flox to replace nvm
---

# Node Version Manager (nvm) migration guide

Flox is an environment and package manager that allows you to install software from an extensive catalog into individual [environments][environment_concept]{:target="\_blank"}, each of which usually corresponds to a software project. Flox gives you the opportunity to simplify the development workflow used by your team, consolidating various functions into a single command: `flox activate`.

Just like [nvm](https://github.com/nvm-sh/nvm){:target="\_blank"}, Flox allows you to install and activate different versions of Node.js, enabling you to switch versions as project requirements dictate. _Unlike_ nvm, however, Flox also allows you to install just about any software you need, including databases and packages from language ecosystems like Python, Rust, Go, Java, Ruby, and others.

## Why you might want to use Flox instead of nvm

nvm does exactly what it purports to do: it manages Node.js versions simply and effectively. Point notwithstanding, it's also one more dependency that you don't have to worry about if you're using Flox. Consider whether one of the following cases applies to you, or to your team:

* **You work on a team with members who have diverse skill sets, and you want to have a single entrypoint for development, regardless of language ecosystem.** No matter what languages and technologies your team is comfortable with, they can use the same Flox commands to spin up their local dev environments. For example, instead of asking a Java developer who uses a Linux machine to install nvm in order to get the right node version for your project, you can offer a better solution. That developer can use the same Flox commands they use to activate their own projects to activate the dev environment for your node project, which you develop on your Mac.
* **You want a tool that allows you to manage Node.js versions as well as other dependencies.** Having a single-use tool like nvm is fine, but what if you could install node, PostgreSQL, nginx, etc. with a single command? Flox lets you do just that. It also [allows you to configure and run services][services]{:target="\_blank"}, the latter of which you can do simply by adding the `--start-services` argument to `flox activate`.
* **You need to use [`node-gyp`](https://github.com/nodejs/node-gyp){:target="\_blank"} to compile native add-on modules for Node.js, and you want to be sure you have the right version of Python, [Make](https://www.gnu.org/software/make/){:target="\_blank"}, [GCC](https://gcc.gnu.org/){:target="\_blank"}, [Clang](https://clang.llvm.org/get_started.html), and other dependencies.** As a Flox user, you can be certain you'll install versions of these dependencies that are compatible with the node version in your environment. This is all thanks to Nix Packages, which is the underlying software repository on which the Flox Catalog is based.
* **You need to manage versions of other JavaScript runtimes, like Bun or Deno.** While nvm is, as the name denotes, used for managing Node.js versions, that's all it does. You can use Flox to install node, but you can also use it to install different JavaScript runtimes, including [Bun](https://bun.sh/){:target="\_blank"} and [Deno](https://deno.com/){:target="\_blank"}.

## Install Flox

Download and install Flox as described in our [installation instructions][install_flox]{:target="\_blank"}.

## Create a Flox environment in your existing project and install Node.js

Navigate to your project's directory and run this command to initialize a Flox environment:

```{ .sh .copy }
flox init
```

After that's done, you can search for the version of Node.js that is currently included in your `.nvmrc`, or in the `"engines"` property of your `package.json`. (Note that node is listed as `nodejs` and variants thereof in the Flox Catalog.)

```{ .sh .copy }
flox search nodejs
```

When you search for Node.js, you'll see output like this in your terminal:

```console
➜  node-project git:(main) ✗ flox search nodejs
nodejs       Event-driven I/O framework for the V8 JavaScript engine
nodejs_14    Event-driven I/O framework for the V8 JavaScript engine
nodejs_16    Event-driven I/O framework for the V8 JavaScript engine
nodejs_18    Event-driven I/O framework for the V8 JavaScript engine
nodejs_19    Event-driven I/O framework for the V8 JavaScript engine
nodejs_20    Event-driven I/O framework for the V8 JavaScript engine
nodejs_21    Event-driven I/O framework for the V8 JavaScript engine
nodejs_22    Event-driven I/O framework for the V8 JavaScript engine
nodejs_23    Event-driven I/O framework for the V8 JavaScript engine
nodejs-10_x  Event-driven I/O framework for the V8 JavaScript engine

Showing 10 of 67 results. Use `flox search nodejs --all` to see the full list.

Use 'flox show <package>' to see available versions
```

There is _a lot_ of software in the Flox Catalog, so you should have no trouble finding the node version you need. We recommend that you install one of the `nodejs` packages with a numerical suffix (e.g., `nodejs_18` or `nodejs_22`), rather than `nodejs`, which is the latest stable version of node from the perspective of the Nix Packages maintainers. The `nodejs` package may not get a new version until all the other Nix packages that depend on that specific Node.js version have been updated for compatibility, which could be a long while after an official Node.js release.

At any rate, for this project, perhaps you decide to install Node.js v20.18.1. You can start by running the following command:

```{ .sh .copy }
flox install nodejs_20
```

This should yield the following output:

```console
➜  node-project git:(main) ✗ flox install nodejs_20
✅ 'nodejs_20' installed to environment 'node-project'
```

## Verify the Node.js version

Now that you've installed node, you activate the Flox environment to verify that it has the the version you expect.

```{ .sh .copy }
flox activate
```

When you activate the environment, you'll see output like this in your terminal:

```console
➜  node-project git:(main) ✗ flox activate
✅ You are now using the environment 'node-project'.
To stop using this environment, type 'exit'
```

Within the active Flox environment, you can verify the node version as follows:

```{ .sh .copy }
node -v
```

This command should give you the output you expect, namely the version of node available in your shell:

```console
flox [node-project] ➜  node-project git:(main) ✗ node -v
v20.18.1
```

## Add Node.js and associated dependencies to a package group (optional)

If you need an older version of node in your environment, we recommend that you specify a package group in your manifest to ensure that you can still install the latest versions of other software in your environment. (For more on the manifest and on package groups, read [our reference guide][manifest]{:target="\_blank"}.)

At this point, you should run the following command to edit the Flox environment configuration manually:

```{ .sh .copy }
flox edit
```

Now you can edit the `manifest.toml` as illustrated below.

```toml
...
[install]
nodejs_20 = { pkg-path = "nodejs_20", pkg-group = "node-toolchain" }
...
```

## Install other dependencies using Flox (optional)

Assuming your project is like most Node.js applications, you probably have dependencies other than node to install. In this case, maybe you need PostgreSQL and nginx. Fortunately, you can install both using Flox, in the same way in which you installed node.

```{ .sh .copy }
flox install postgresql nginx
```

Running this command will install both dependencies to the Flox environment.

```console
flox [node-project] ➜  node-project git:(main) ✗ flox install postgresql nginx
✅ 'postgresql' installed to environment 'node-project'
✅ 'nginx' installed to environment 'node-project'
```

Now you have everything you need to develop locally, and you didn't have to figure out how to install [nginx](https://nginx.org/en/docs/install.html){:target="\_blank"} and [PostgreSQL](https://www.postgresql.org/download/){:target="\_blank"} individually.

## Update the Node.js version

If you want to install a different node version, you can always update your environment to include the version you need. For example, let's say you're upgrading your project to Node.js v22. The best way to get the correct Flox Catalog version name for your desired version is to run `flox show <package>`:

```{ .sh .copy }
flox show nodejs_22
```

Now you can see all the available versions of Node.js v22 in the Flox Catalog.

```console
flox [node-project] ➜  node-project git:(main) ✗ flox show nodejs_22
nodejs_22 - Event-driven I/O framework for the V8 JavaScript engine
    nodejs_22@nodejs-22.10.0
    nodejs_22@nodejs-22.9.0
    nodejs_22@nodejs-22.8.0
    nodejs_22@nodejs-22.6.0
    nodejs_22@nodejs-22.5.1
    nodejs_22@nodejs-22.4.1
    nodejs_22@nodejs-22.3.0
    nodejs_22@nodejs-22.2.0
    nodejs_22@nodejs-22.0.0

```

Once you know what's available, you can run the edit command to open up the manifest for the environment:

```{ .sh .copy }
flox edit
```

You can now set your desired node version directly in the manifest, and then save your changes. Note that you'll need to prepend `nodejs-` to whatever Node.js version number you intend to set in the manifest. This is required because of how those versions are stored in the Nix Packages collection.

(If you omit the specific version, you will get the latest version of `nodejs_22` that's compatible with everything in your environment. If you have a `pkg-group` set but no specific `version`, you'll get the latest version that's compatible with the rest of the software in the package group.)

```toml
...
[install]
nodejs_22 = { pkg-path = "nodejs_22", pkg-group = "node-toolchain", version = "nodejs-22.10.0" }
...
```

## Update the README in your project

At this point, you can replace any nvm-related instructions in your README with corresponding instructions for using Flox. In particular, instead of running `nvm use` to pick up the Node.js version from the `.nvmrc`, you can just run `flox activate`. This will install all the dependencies in your Flox environment, not just node.

## Remove nvm and related artifacts

Now that you're managing your project's Node.js version using Flox, you can `git rm .nvmrc` and commit the result. You're free to repeat the process in other project directories before following the [instructions for uninstalling nvm as listed in the nvm README](https://github.com/nvm-sh/nvm?tab=readme-ov-file#uninstalling--removal){:target="\_blank"}.

[environment_concept]: ../../concepts/environments.md
[install_flox]: ../../install-flox/install.md
[manifest]: ../../man/manifest.toml.md
[services]: ../../concepts/services.md

---


## Understanding Organizations in FloxHub

> Source: `concepts/organizations.md`

--8<-- "paid-feature.md"

An **organization** in [FloxHub][floxhub_concept] represents a shared workspace for teams. It provides:

- A private catalog
- Scoped access control
- A foundation for collaboration among multiple users

This document outlines how organizations work today, and how they can be managed.

## User Membership

A user can belong to more than one organization. This allows users to use a single FloxHub account in multiple contexts.

## Permissions and Access Control

Organizations in FloxHub use role-based access control (RBAC) to assign permissions to organization members. A user can have one of the following roles within an organization:

- **Owner**: Full administrative access, including managing members and settings.
- **Writer**: Can create and update environments and packages, but cannot manage members or organization settings.
- **Reader**: Can view and pull environments and can install packages, but cannot create or modify them.

The organization must have at least one owner, but may have multiple. Owners can manage the organization, including adding or removing members and changing roles. Owners may not modify their own role or remove themselves from the organization.

## Machine Access Tokens

In addition to _user-level_ access based on FloxHub accounts, FloxHub supports _programmatic_ access via `Auth0`-issued machine tokens, using the client credentials grant. These tokens are not tied to users—they authenticate as the organization itself and are intended for CI/CD or other non-interactive use cases.

FloxHub supports this via the client credentials grant. To enable it, contact the Flox team to request a client ID and secret. Once provisioned, your workflows can fetch an access token using a `curl` command:

```{ .sh .copy }
curl --request POST \
  --url https://auth.flox.dev/oauth/token \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data "client_id=YOUR_CLIENT_ID" \
  --data "client_secret=YOUR_CLIENT_SECRET" \
  --data "audience=https://hub.flox.dev/api" \
  --data "grant_type=client_credentials"
```

The token can be used to authenticate calls to FloxHub’s API or CLI tools in the context of your organization.

## Environment Visibility and Management

Organizations in FloxHub include a view of all environments and packages owned by the organization.

For each environment, users can:

- See the live generation and a history of changes
- Configure basic settings, such as owner and name
- Delete environments

For each package, users can:

- See package details, including supported systems and available versions

Environments and packages created within an organization are visible to all its members, with access governed by the organization’s RBAC configuration.

[floxhub_concept]: ./floxhub.md

---


## Paid Feature

> Source: `snippets/paid-feature.md`

This is a paid feature included with Flox for Teams.

---


## manifest.toml

> Source: `concepts/publishing.md`

---
title: "Publishing"
description: Understanding how to publish packages with Flox
---

Once you've built a package with the [`flox build`][flox-build] command, you likely want to _use_ it somewhere.
The [`flox publish`][flox-publish] command gives you the ability to upload packages to your private catalog so that you can _install_ them into your environments.
In order to share packages with other people you must create an organization.
See the [organizations][organizations-concept] page for more details.

## Uploading a package

The `flox publish <name>` command allows you to upload a package built with the `flox build` command, where `<name>` is the name of any build listed in the `build` section of the manifest.

```toml
# manifest.toml
[build.mypkg]
command = '''
  ...
'''
```

```{ .sh .copy }
flox publish mypkg
```

## Publish process

In order to make sure that the uploaded package can be built reproducibly,
Flox imposes some constraints on the build and publish process.

- The Flox environment performing the build must tracked in a git repository.
- Tracked files in the git repository must be clean.
- The git repository has a remote defined, and the current revision has been pushed to it.
- The Flox environment must have at least one package installed to it.

All of this is there to ensure that the published package can be locked to a point in time in the Base Catalog and an upstream source revision.
As a reminder, the Base Catalog is the built-in [Catalog][catalog-concept] provided by Flox.

As part of the `flox publish` command, the CLI will clone the git repository to a temporary directory to ensure that any files referenced in the build are tracked by the repository.
A clean `flox build` is then run in this directory.

If the build completes successfully, the package, its closure (all the software it depends on), and its metadata are uploaded to your Catalog.

## The published payload

A published package consists of two parts:

- The package metadata
- The package itself

The package metadata is uploaded to Flox servers so that the Flox CLI can see that it's available via the [`flox search`][flox-search], [`flox show`][flox-show], and [`flox install`][flox-install] commands.
The package itself is uploaded to a Catalog Store.

A Catalog Store is effectively a cache for published packages, and Flox provides one by default.
An organization can choose to provide their own Catalog Store in the form of an S3-compatible storage provider.
In this case, it means that your organization has complete control over your packages and they will never be stored by Flox.
To pursue this option, contact Flox directly.

## Consuming published packages

Once you have uploaded a package via `flox publish`, the package becomes available in `flox search`, `flox show`, and `flox install`.
To distinguish these packages from those provided by the Base Catalog, published packages are prefixed with the name of the user or organization.
For example, if your user is called `myuser` and you publish a package named `hello`, the package will appear as `myuser/hello` in the Flox CLI.

When a user runs `flox install myuser/hello`, the package is downloaded directly from the Catalog Store that it was published to.
If organizations configure their own Catalog Store (rather than using the default Catalog Store provided by Flox), it is never downloaded to or cached on Flox servers.

### Sharing

--8<-- "paid-feature.md"

Sharing packages with multiple users is only possible with an organization.
This means that individual users will not be able to share packages they've published with other users.

Packages can be published to an organization's catalog with
`flox publish --org <organization>`.
Packages published to an organization's catalog are visible to all other members
of the organization,
but they cannot be viewed by anyone outside the organization.
For anyone in the organization, published packages become available in
`flox search`, `flox show`, and `flox install`.

[builds-concept]: ./builds.md
[catalog-concept]: ./packages-and-catalog.md
[flox-build]: ../man/flox-build.md
[flox-publish]: ../man/flox-publish.md
[flox-search]: ../man/flox-search.md
[flox-show]: ../man/flox-show.md
[flox-install]: ../man/flox-install.md
[organizations-concept]: ./organizations.md

---


## Python

> Source: `languages/python.md`

---
title: Python
description: Common questions and solutions for using Python with Flox
---

# Python

This provides an overview of how to create Flox environments for new or existing Python projects.

## Using Flox in a new project

Getting started with Flox is super simple. First, create and/or `cd` into your project directory.

```{ .sh .copy }
mkdir new-python-project && cd new-python-project
```

Next, initialize your Flox environment:

```{ .sh .copy }
flox init
```

This will suggest a few commands you can run next:

```console
$ flox init
✨ Created environment 'new-python-project' (x86_64-linux)

Next:
  $ flox search <package>    <- Search for a package
  $ flox install <package>   <- Install a package into an environment
  $ flox activate            <- Enter the environment
  $ flox edit                <- Add environment variables and shell hooks
```

This Flox environment is now ready to be populated with packages.

### Select a Python interpreter

To begin, we need a Python interpreter. For this example, we will be using Python 3.11. Search for the version of Python your project requires, omitting the dot between major and minor numbers:

```{ .sh .copy }
flox search python311
```

This will show you the list of packages matching the major and minor version of Python you specified:

```console
$ flox search python311
python311      High-level dynamically-typed programming language
python311Full  High-level dynamically-typed programming language

Use 'flox show <package>' to see available versions
```

To see the specific versions of Python available in the Flox Catalog, use the `flox show` command:

```{ .sh .copy }
flox show python311Full
```

This will list all of the releases that match the major and minor numbers you provided:

```console
$ flox show python311Full
python311Full - High-level dynamically-typed programming language
    python311Full@python3-3.11.9
    python311Full@python3-3.11.8
    python311Full@python3-3.11.7
    python311Full@python3-3.11.6
    python311Full@python3-3.11.5
    python311Full@python3-3.11.4
    python311Full@python3-3.11.3
    python311Full@python3-3.11.2
    python311Full@python3-3.11.1
```

At this point, you can install the latest version by running `flox install` without a version specified:

```{ .sh .copy }
flox install python311Full
```

This will show a message indicating the package was successfully installed:

```console
$ flox install python311Full
✅ 'python311Full' installed to environment 'new-python-project'
$ flox list
python311Full: python311Full (python3-3.11.9)
```

When `flox upgrade` is run in this environment, the version of Python will be upgraded to the latest version available in the catalog matching those major and minor numbers. If you wish to pin your Flox environment to a specific release of Python, you can specify it in the `flox install` command:

```{ .sh .copy }
flox install python311Full@python3-3.11.3
```

### Add Python packages

Python projects often require a collection of packages in addition to an interpreter. Often these are installed using `pip`, but they can also be acquired from the Flox Catalog. This will allow them to be locked in the Flox Manifest alongside the other packages in your environment.

To find these Python packages in the Flox Catalog, use the same `flox search` syntax from before:

```{ .sh .copy }
flox search numpy
```

This will return the set of packages that match your search term:

```console
$ flox search numpy
[...]
python311Packages.numpy    Scientific tools for Python
[...]
```

Python packages will have a prefix of `pythonXXXPackages.` in their package name, with `XXX` matching the version of Python you have installed into your environment. To install them, use the entire package name including the prefix:

```{ .sh .copy }
flox install python311Packages.numpy python311Packages.pandas
```

You will see output indicating that the packages were successfully installed. If installation was not successful, you should see an error message indicating the failure:

```console
$ flox install python311Packages.numpy python311Packages.pandas
✅ 'numpy' installed to environment 'new-python-project'
✅ 'pandas' installed to environment 'new-python-project'
```

### Activate the new environment

Once the packages have been installed, activate the new environment:

```{ .sh .copy }
flox activate
```

This will put you into a new subshell with your environment active:

```console
$ flox activate
✅ You are now using the environment 'new-python-project'.
To stop using this environment, type 'exit'

flox [new-python-project] $
```

## Using Flox in an existing project

If you are working with an existing project that is already configured for Python - e.g. it has a `requirements.txt` or `pyproject.toml` - Flox provides an automated environment setup flow.

For this example we will clone the `eralchemy` repo, which already contains Python configuration:

```{ .sh .copy }
git clone https://github.com/eralchemy/eralchemy.git && cd eralchemy
```

### Auto-initialize the environment

Once inside the `eralchemy` project directory, initialize a new Flox environment:

```{ .sh .copy }
flox init
```

You will see the following question in the output:

```console
$ flox init
Flox detected a Python project with the following Python provider(s):

* pyproject (generic pyproject.toml)

  Installs python (3.12.5) with pip bundled.
  Adds a hook to setup a venv.
  Installs the dependencies from the pyproject.toml to the venv.

! Would you like Flox to set up a standard Python environment?
You can always change the environment's manifest with 'flox edit'
  Yes - with pyproject
  No
> Show suggested modifications
[Use '--auto-setup' to apply Flox recommendations in the future.]
```

When you initialize Flox and it finds a `pyproject.toml` or `requirements.txt` file inside a project directory, it automatically runs this wizard.

Here's what each option does:

- “Yes” builds the environment using the `pyproject.toml` file;
- “No” skips automatic setup. You can use `pip` or `poetry` with `pyproject.toml` to build your environment;
- “Show” previews the configuration you'd get by selecting “Yes,” allowing you to vet your environment's setup.

If you would like to preview the proposed changes, you can choose the "Show" option. It will show you the proposed changes to each section of your environment manifest, e.g.:

```console
> Show suggested modifications for pyproject
[Use '--auto-setup' to apply Flox recommendations in the future.]


[install]
python3.pkg-path = "python3"
python3.version = ">=3.8"

[hook]
on-activate = '''
  # Setup a Python virtual environment

  export PYTHON_DIR="$FLOX_ENV_CACHE/python"
  if [ ! -d "$PYTHON_DIR" ]; then
    echo "Creating python virtual environment in $PYTHON_DIR"
    python -m venv "$PYTHON_DIR"
  fi

  # Quietly activate venv and install packages in a subshell so
  # that the venv can be freshly activated in the profile section.
  (
    source "$PYTHON_DIR/bin/activate"
    # install the dependencies for this project based on pyproject.toml
    # <https://pip.pypa.io/en/stable/cli/pip_install/>
    pip install -e . --quiet
  )
'''

[profile]
bash = '''
  echo "Activating python virtual environment" >&2
  source "$PYTHON_DIR/bin/activate"
'''
fish = '''
  echo "Activating python virtual environment" >&2
  source "$PYTHON_DIR/bin/activate.fish"
'''
tcsh = '''
  echo "Activating python virtual environment" >&2
  source "$PYTHON_DIR/bin/activate.csh"
'''
zsh = '''
  echo "Activating python virtual environment" >&2
  source "$PYTHON_DIR/bin/activate"
'''
```

If you choose “Yes” to accept this configuration, you can edit or customize it once Flox finishes building just by typing `flox edit`. For future projects, you can automate this setup process for Python environments by running:

```{ .sh .copy }
flox init --auto-setup
```

### Add system packages

The only dependency from `pyproject.toml` that Flox did not install for us is [Graphviz](https://graphviz.org/), an open source tool for creating and visualizing graphs.

To do this, we could run `flox edit` and add `graphviz` to the `[install]` section of our environment's software manifest, but it's just as easy to install it from the command line. So let’s do that instead:

```{ .sh .copy }
flox install graphviz
```

Now it's time to put this environment through its paces.

### Activate and verify the environment

First let's activate the environment:

```{ .sh .copy }
flox activate
```

You should see output indicating that the Python virtual environment has been created:

```console
$ flox activate
✅ You are now using the environment 'eralchemy'.
To stop using this environment, type 'exit'

Creating python virtual environment in /home/floxfan/eralchemy/.flox/cache/python
Activating python virtual environment
```

At this point, the version of `eralchemy` is available within your environment.

```console
(python) flox [eralchemy] $ which eralchemy
/home/floxfan/eralchemy/.flox/cache/python/bin/eralchemy
```

## Build with Flox

Not only can you _develop_ your software with Flox, but you can _build_ it as well.
See the [builds][build-concept] concept page for more details.

### Manifest builds

#### Pip

For Python projects using `pip`, a build looks like installing the project to the `$out` directory.

```toml
[build.myproject]
command = '''
  pip install --target=$out .
'''
```

Note the trailing `.` to indicate that you're installing the package in the
current directory.
If you're working in a repository with multiple packages in subdirectories,
you would replace `.` with the path to the package sources.

#### Poetry

For Poetry and tools that create a virtual environment for you, a build entails installing the virtual environment to `$out`.
Poetry in particular does not allow you to choose the location (or name) of the virtual environment directory itself, but it does allow you to configure the _parent_ directory of the virtual environment.
The build command shown below uses environment variables to tell Poetry to use the `$out` directory as the parent of the virtual environment.
After running `poetry install` you should have a directory structure that looks like this:

```console
$out/
  myproject-<hash>-py3.12/
    ...
```

Since Poetry doesn't let you decide where _exactly_ this virtual environment belongs, you need to symlink any executables from the virtual environment into the `$out/bin` directory yourself to ensure that the build output adheres to the Filesystem Hierarchy Standard (FHS).
You also need to install a Python interpreter and add it to `runtime-packages` so that the virtual environment can reference it.

The full manifest for a build using Poetry is shown below:

```toml
version = 1

[install]
python3.pkg-path = "python3"
python3.version = ">=3.12"
poetry.pkg-path = "poetry"

[build.myproject]
command = '''
  # Install to a new virtualenv.
  export POETRY_VIRTUALENVS_PATH=$out
  export POETRY_VIRTUALENVS_IN_PROJECT=false
  export POETRY_VIRTUALENVS_OPTIONS_NO_PIP=true
  poetry install

  # Symlink any executables from the virtualenv.
  mkdir -p "${out}/bin"
  cd $out/bin
  ln -s ../*/bin/myproject .
'''
runtime-packages = [
  "python3",
]
```

[build-concept]: ../concepts/builds.md

---


## Ruby

> Source: `languages/ruby.md`

---
title: Ruby
description: Common questions and solutions for using Ruby with Flox
---

# Ruby

## Build with Flox

Not only can you _develop_ your software with Flox, but you can _build_ it as well.
See the [builds][build-concept] concept page for more details.

### Manifest builds

Since Ruby is not a compiled language, to create an executable artifact you must create a shell script that calls `bundle exec`. Configure bundler to use the local directory to store the bundles by setting `$GEM_HOME` to something like `./vendor`. If you're Gemfile compiles native extensions, you may also want to `unset CPATH`. See the [Flox ruby environment](https://hub.flox.dev/flox/ruby) for more information, examples and specific details.

For example, say you have an application whose source is in `app.rb`, and that you created a script called `myproject` at the root of your repository with the following contents:

```bash
#!/usr/bin/env bash

bundle exec ruby app.rb
```

The build command for your application would look like this:

```toml
[build.myproject]
command = '''
  # Vendor dependencies
  bundle

  # Create the output directories
  mkdir -p $out/{lib,bin}

  # Copy source files to $out/lib
  cp -pr * $out/lib

  # Move the executable script
  mv $out/lib/myproject $out/bin/myproject
'''
```

#### Vendoring dependencies in pure builds

As discussed in the [pure builds][pure-builds-section] of the Builds concept page, pure builds run in a sandbox without network access on Linux.
A pure build can be run as a multi-stage build where the first step vendors dependencies.
An example is shown below:

```toml
[build.myproject-deps]
command = """
   # Don't use or update paths in the real project config.
   export BUNDLE_IGNORE_CONFIG=true

   # Pre-fetch the deps outside of the sandbox.
   export BUNDLE_PATH=$out
   export BUNDLE_CACHE_PATH=${out}/cache
   bundle cache --no-install

   # These gems appear to be duplicated irrespective of `--no-install`
   rm -rf $out/ruby
"""

[build.myproject]
command = """
   mkdir -p $out/{lib,bin}

   # Don't use or update paths in the real project config.
   export BUNDLE_IGNORE_CONFIG=true

   # Perform an isolated install using pre-fetched deps.
   export BUNDLE_PATH=$out/lib/vendor
   export BUNDLE_CACHE_PATH=${myproject-deps}/cache
   export BUNDLE_DEPLOYMENT=true
   bundle install --standalone --local

   cp Gemfile Gemfile.lock $out/lib
   cp app.rb quotes.json $out/lib
   cp quotes $out/bin/myproject
"""
sandbox = "pure"
```

[build-concept]: ../concepts/builds.md
[pure-builds-section]: ../concepts/manifest-builds.md#pure-builds

---


## Rust

> Source: `languages/rust.md`

---
title: Rust
description: Common questions and solutions for using Rust with Flox
---

# Rust

## What do I need for a basic environment?

First we'll show you the answer, and then we'll explain.
The full example environment can be found in the [floxenvs repository][example_env].

A manifest that provides you a Rust development environment would look like
this:

```toml title="Rust development environment"
version = 1

[install]
# Rust toolchain
cargo.pkg-path = "cargo"
cargo.pkg-group = "rust-toolchain"
rustc.pkg-path = "rustc"
rustc.pkg-group = "rust-toolchain"
clippy.pkg-path = "clippy"
clippy.pkg-group = "rust-toolchain"
rustfmt.pkg-path = "rustfmt"
rustfmt.pkg-group = "rust-toolchain"
rust-lib-src.pkg-path = "rustPlatform.rustLibSrc"
rust-lib-src.pkg-group = "rust-toolchain"
libiconv.pkg-path = "libiconv"
libiconv.systems = ["aarch64-darwin", "x86_64-darwin"]

# rust-analyzer goes in its own group because it's updated
# on a different cadence from the compiler and doesn't need
# to match versions
rust-analyzer.pkg-path = "rust-analyzer"
rust-analyzer.pkg-group = "rust-analyzer"

# Linker
gcc.pkg-path = "gcc"
gcc.systems = ["aarch64-linux", "x86_64-linux"]
clang.pkg-path = "clang"
clang.systems = ["aarch64-darwin", "x86_64-darwin"]

[vars]

[hook]

[profile]

[options]
systems = ["aarch64-darwin", "x86_64-darwin", "aarch64-linux", "x86_64-linux"]
```

The typical Rust developer probably uses [rustup][rustup] to manage their
toolchains.
Flox aims to be an all-in-one solution, so you'll use Flox instead of `rustup`.
The main difference here is that the toolchain components are unbundled in
Flox,
so you'll need to install `cargo` and `rustc` as independent packages.
Some common packages you'll want to install are:

- `cargo`
- `rustc`
- `rustfmt`
- `clippy`
- `gcc` on Linux, `clang` on macOS
- `libiconv` on macOS
- `rustPlatform.rustLibSrc`
- `rust-analyzer`

Let's explain some of those packages.

`cargo` is self-explanatory, it's the default build tool for Rust.
However, all Flox packages automatically install all of their dependencies,
so `cargo` also installs `rustc` on its own.
If that's the case, why do we need a `rustc` package?
The short answer is build scripts (`build.rs` files).

One of the ways that Flox makes environments deterministic and reproducible
is that packages don't expose their dependencies to `PATH`,
so `cargo` doesn't expose its `rustc` to `PATH`.
This is fine in most cases since you often don't need to call `rustc` yourself,
but this becomes an issue for crates that contain `build.rs` build scripts that
manually invoke `rustc`.
However, even if your crate doesn't have a `build.rs`,
it is very common for a transitive dependency to need to link to system
libraries such as `openssl`.
This is why we install a separate `rustc` package.
You may also find that you need to install a `pkg-config` package if some
system libraries aren't found.

Build scripts are also why we install the `gcc` or `clang` package:
build scripts often call out to linkers in addition to `rustc`.

The `libiconv` package is necessary on macOS because the Rust standard library
links against it on macOS.
The `rustPlatform.rustLibSrc` provides the source code for `std` so that
`rust-analyzer` can provide diagnostics and documentation for standard library
code.

As a final step, you want to make sure that your Rust toolchain componenents
share the same exact versions of their dependencies,
so you'll want to add them to a package group
(`rust-toolchain` in the example above).

## Add the `target` directory to `PATH`

If you're developing a binary instead of a library,
you may find it useful to add the `target/debug` or `target/release`
directories to your `PATH` for interactive testing.
That is very simple to do with the `hook.on-activate` section of the manifest:

```toml
[hook]
on-activate = '''
  export PATH="$PWD/target/debug:$PATH"
'''
```

Now if you were developing a binary called `mybin`,
you could call it directly instead of via `target/debug/mybin`,
and it will automatically be kept up to date on every `cargo build`.

## Add `cargo` aliases

The `[profile]` section allows you to add aliases to your development shell
that are available after activating your environment.
If you currently use `make`, `just`, or a `.cargo/config.toml` file to set
provide simple aliaes in your development environment,
you may be able to remove those dependencies and just use the Flox manifest
instead:

```toml
[profile]
bash = '''
  alias build="cargo build"
'''
zsh = '''
  alias build="cargo build"
'''
fish = '''
  alias build "cargo build"
'''
```

## How do I use nightly compilers?

Nightly compilers aren't currently packaged in the Flox Catalog.
If you need to use nightly compilers,
you can use our Nix flake support to prepare a flake that provides a nightly
compiler.
You would need to prepare that flake, call it `github:rust-dev/my-nightly`,
and add it to the manifest as a flake package:

```toml
[install]
rust-nightly.flake = "github:rust-dev/my-nightly"
```

Popular projects used by the Nix community for this purpose are:

- [nix-community/fenix][fenix]
- [oxalica/rust-overlay][rust-overlay]

[rustup]: https://rustup.rs
[fenix]: https://github.com/nix-community/fenix
[rust-overlay]: https://github.com/oxalica/rust-overlay

An example flake is provided at [zmitchell/rust-toolchains][custom-toolchains].
This flake uses `fenix` to provide three different toolchains:

- `stable`, which tracks the latest stable release of Rust
- `nightly`, which tracks the latest nightly release of Rust
- `esp32-riscv-no-std`, which provides a nightly toolchain with support for the [ESP32-C3][esp32], a microprocessor based on the [RISC-V][risc-v] architecture.

You are encouraged to fork that repository and use the examples to provide your own custom Rust toolchains.
It includes a GitHub Action that runs daily to keep up to date with the latest Rust releases.

## Build with Flox

Not only can you _develop_ your software with Flox, but you can _build_ it as well.
See the [builds][build-concept] concept page for more details.

### Manifest builds

Since the output of the build must be copied to the `$out` directory, you'll need to copy the compiled executable out of the `target` directory and into `$out`.
There is an unstable environment variable in Cargo that will allow you to set the output directory of the build, but we'll stick to stable features here:

```toml
[build.myproject]
command = '''
  cargo build --release
  mkdir -p $out/bin
  cp target/release/myproject $out/bin/myproject
'''
```

#### macOS builds require libiconv

Rust executables built for macOS link against the `libiconv` library, which is used for some Unicode operations.
This library is provided by macOS, and the large majority of Rust packages on macOS link against this library already, so this is not a dependency introduced by building via Flox.
For reproducibility you must include this package as a dependency rather than depending on being able to locate the library on the system at runtime.

If you build rust applications on macOS, add the following to the manifest under `[install]`:

```toml title="manifest.toml"
libiconv.pkg-path = "libiconv"
libiconv.systems = ["aarch64-darwin", "x86_64-darwin"]
```

#### Linux builds require GCC

On Linux, Rust executables link against `libgcc` for stack unwinding.
`libgcc` is provided as part of the `gcc` package, which means that `gcc` needs to be available to your package at runtime on Linux.
This happens by default if the `gcc` package is installed in the `toplevel` (default) package group, i.e. there is no `pkg-group` set.

```toml title="manifest.toml"
gcc.pkg-path = "gcc"
gcc.systems = ["aarch64-linux", "x86_64-linux"]
```

If `runtime-packages` is set for this package, `gcc` must be included in the list of included packages.

```toml title="manifest.toml"
[build.myproject]
…
runtime-packages = [… "gcc"]
```

    Depending on the `gcc` package at runtime includes `libgcc`, the compiler, its manpages, etc when in reality the package only depends on `libgcc` at runtime on Linux. This limitation will be addressed in the future.

#### Vendoring dependencies in pure builds

As discussed in the [pure builds][pure-builds-section] of the Builds concept page, pure builds run in a sandbox without network access on Linux.
A pure build can be run as a multi-stage build where the first step vendors dependencies.
An example is shown below:

```toml
[build.myproject-deps]
command = '''
  mkdir -p $out/etc
  cargo vendor $out/etc/vendor
'''

[build.myproject]
command = '''
  # Create a .cargo/config.toml to tell Cargo to use the vendored
  # dependencies.
  mkdir -p .cargo
  cat <<-'EOF' > .cargo/vendor-config.toml
  [source.crates-io]
  replace-with = "vendored-sources"

  [source.vendored-sources]
  directory = "${myproject-deps}/etc/vendor"
EOF

  # Perform the build
  mkdir -p $out/bin
  cargo build --release --offline --config .cargo/vendor-config.toml
  cp target/release/myproject $out/bin/myproject
'''
sandbox = "pure"
runtime-packages = ["libiconv", "gcc"]
```

### Nix expression builds

To build a project using [`buildRustPackage`](https://nixos.org/manual/nixpkgs/stable/#rust) which will import your existing dependency file:

```nix
{ rustPlatform }:

rustPlatform.buildRustPackage {
  pname = "myproject";
  version = "0.0.1";
  src = ../../../.;

  cargoLock = {
    lockFile = src + "/Cargo.lock";
  };
}
```

[example_env]: https://github.com/flox/floxenvs/tree/main/rust
[custom-toolchains]: https://github.com/zmitchell/rust-toolchains
[esp32]: https://www.espressif.com/en/products/socs/esp32
[risc-v]: https://en.wikipedia.org/wiki/RISC-V
[build-concept]: ../concepts/builds.md
[pure-builds-section]: ../concepts/manifest-builds.md#pure-builds

---


## Self Managed

> Source: `k8s/install/self-managed.md`

---
title: "Self-managed Kubernetes"
description: "Installing Imageless Kubernetes to a self-managed Kubernetes cluster"
---

This guide describes general steps for installing Imageless Kubernetes, suitable for self-managed clusters or other Kubernetes distributions (e.g. K3s).

To use Imageless Kubernetes, on each node you will need to:

- Install Flox
- Install the Flox `containerd` runtime shim
- Register the shim with `containerd`
- Register the shim with Kubernetes


## Node configuration

### Flox installation

Flox packages and installation instructions for `rpm` and `deb` based distributions are available from the the [Install Flox][install-flox] page.

Flox will need to be installed on each node that will host Imageless Kubernetes pods.

### Runtime shim installation

For most Kubernetes distributions, the automatic installation method is the recommended option. We also provide a manual method for those that are not supported by the automatic installer.

We recommend first trying the automatic method, and only moving to the manual method if issues are encountered.

#### Automatic installation

We provide an installer in the form of a Flox environment that deploys Imageless Kubernetes by:

- Detecting the installed `containerd` version
- Downloading and installing the correct runtime shim version
- Updating the `containerd` configuration as necessary
- Restarting `containerd`

Details about the installer can be found on its [FloxHub page][shim-installer]; the script is executed by the activation hook for the environment.

Once Flox is installed, the runtime shim can be installed by running the following command as `root` on each node that will host Imageless Kubernetes pods.

```sh
flox activate -r flox/containerd-shim-flox-installer --trust
```

#### Manual installation

If you receive a message like:

```sh
containerd not found, skipping flox shim installation
```

when running the installer, but do have `containerd` installed, you can perform the installation process manually.

This may be necessary for Kubernetes distributions like K3s that vendor `containerd`, and put its binaries and configuration in a non-standard location.

1. Create a Flox environment and install the runtime shim.

    ```sh
    mkdir containerd-shim-flox
    cd containerd-shim-flox
    flox init -b
    # use -2x for containerd 2.x, and -17 for 1.7
    flox install flox/containerd-shim-flox-2x
    ```

2. Create a symlink from the Flox environment to `/usr/local/bin`.

    ```sh
    ln -s $PWD/.flox/run/x86_64-linux.containerd-shim-flox.run/bin/containerd-shim-flox-v2 /usr/local/bin/containerd-shim-flox-v2

    ```

3. Add the Flox runtime configuration to the `containerd` `config.toml`.
Check the `version` line at the beginning of the file and use the matching configuration below.

            This is usually in `/etc/containerd`, but on K3s, it is in `/var/lib/rancher/k3s/agent/etc/containerd`.

        See the [K3s documentation](https://docs.k3s.io/advanced#configuring-containerd) for more details on that specific implementation.

    ```toml title="version = 2"
    [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.flox]
        runtime_path = "/usr/local/bin/containerd-shim-flox-v2"
        runtime_type = "io.containerd.runc.v2"
        pod_annotations = [ "flox.dev/*" ]
        container_annotations = [ "flox.dev/*" ]
    [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.flox.options]
        SystemdCgroup = true
    ```

    ```toml title="version = 3"
    [plugins."io.containerd.cri.v1.runtime".containerd.runtimes.flox]
      runtime_path = "/usr/local/bin/containerd-shim-flox-v2"
      runtime_type = "io.containerd.runc.v2"
      pod_annotations = [ "flox.dev/*" ]
      container_annotations = [ "flox.dev/*" ]
    [plugins."io.containerd.cri.v1.runtime".containerd.runtimes.flox.options]
        SystemdCgroup = true
    ```

4. Restart `containerd`

    ```sh
    systemctl restart containerd
    # if needed
    systemctl restart k3s
    ```

## Kubernetes configuration

A [RuntimeClass][runtime-class] is used to expose the runtime to Kubernetes such that it can be utilized to create pods.

We recommend labeling nodes that have the runtime shim installed to ensure Flox pods are only scheduled on them.

1. Label your nodes with the following command:

    ```sh
    kubectl label node <node-name> "flox.dev/enabled=true"
    ```

2. Update the `nodeSelector` in the following `RuntimeClass` definition to match the `label` specified above.

    ```yaml title="RuntimeClass.yaml"
    apiVersion: node.k8s.io/v1
    kind: RuntimeClass
    metadata:
      name: flox
    handler: flox
    scheduling:
      nodeSelector:
        flox.dev/enabled: "true"
    ```

3. Apply this resource with the following command:

    ```sh
    kubectl apply -f RuntimeClass.yaml
    ```

The `nodeSelector` ensures that Flox pods will only be scheduled on nodes with the Flox runtime installed.

## Conclusion

Once the nodes have Flox and the shim installed, you are ready to create pods using the Flox runtime.

A sample `Pod` manifest is available in the [Introduction][intro-section], but any Kubernetes resource that creates a pod (e.g. `Deployment`) can be used by setting the `runtimeClassName` parameter to `flox`.

[intro-section]: ../intro.md
[install-flox]: ../../install-flox/install.md
[shim-installer]: https://hub.flox.dev/flox/containerd-shim-flox-installer
[runtime-class]: https://kubernetes.io/docs/concepts/containers/runtime-class/

---


## Signing keys

> Source: `customer/signing-keys.md`

---
title: Signing keys
description: Create and use signing keys to sign built artifacts
---

# Signing keys

In order to upload a package it must be signed, and in order to install a package published to a Flox Catalog you must configure your system to trust the public key used to sign the package.
By default, packages are signed with a key that's included with the Flox installer, so Flox is configured to be able to install user-published packages out of the box.

However, if you're providing your own Catalog Store, then you must

- Create the signing keys
- Distribute the private key to users trusted to publish packages
- Distribute the public key to users allowed to install those packages
- Have those users configure their systems to trust the public key

## Create a signing key pair

Use the `nix` CLI to generate a private key:

```{ .sh .copy }
nix key generate-secret --key-name signing-key > signing-key.key
```

Then generate a public key from the private key:

```{ .sh .copy }
nix key convert-secret-to-public < signing-key.key > signing-key-pub.key
```

## Sign packages to upload artifacts

Once you've generated the key, you can configure Flox to sign the packages
you publish with that (private) key:


```{ .sh .copy }
flox config --set publish.signing_private_key "/path/to/signing-key.key"
```

If you need to use a different signing key (for example, to publish to a different catalog), you can use the `--signing-key` option with the `flox publish` command.
The private key is necessary for uploading artifacts, so anyone that needs that capability will need access to the key.
One solution is to put the key in a password manager and grant access to users that need to publish.

## Trust a public key to install published artifacts

In order to install a published package you must configure your system to trust the corresponding public key that the artifact was signed with.
This amounts to adding the public key to the list of `extra-trusted-public-keys` in your Nix configuration.

### Add a new trusted key

#### Nix installed via Flox, or standalone Nix installation

If you installed Nix as part of your Flox installation, you need to edit your `/etc/nix/nix.conf` to add a new entry to the `extra-trusted-public-keys` option.
If `/etc/nix/nix.conf` doesn't exist, create it.
If the `extra-trusted-public-keys` option doesn't exist, create it.
This option is a space-delimited list of trusted public keys.

Add the following line, where `<key contents>` is the contents of the signing public key file and `<existing keys>` is any keys that were already populated for this option (if it existed):

```text
extra-trusted-public-keys = <existing keys> <key contents>
```

Note that you do not need quotes around keys in the `extra-trusted-public-keys` option.
In order for the newly trusted key to take effect, the Nix daemon needs to be restarted.
On Linux the daemon is managed via `systemd`, so you can restart it with the following command:

```{ .sh .copy }
sudo systemctl restart nix-daemon
```

On macOS the Nix daemon is managed via `launchd`, so you can restart it with the following command (note that you have to run the command twice, this is not a typo):

```{ .sh .copy }
sudo launchctl kickstart -k system/org.nixos.nix-daemon;
sudo launchctl kickstart -k system/org.nixos.nix-daemon
```

#### NixOS, nix-darwin, or home-manager

For systems whose configuration is managed with Nix, you need to add the public key to the list of trusted public keys in your system configuration.
For NixOS, `nix-darwin`, and `home-manager` the configuration option is the same:

```nix
nix.settings.trusted-public-keys = [
  "<key contents>"
];
```

Once this setting has been edited, rebuild and switch into your new configuration.

### Verify that the key is now trusted

Now verify that the daemon has been restarted and picked up the new key.
You can do this by printing out the daemon's current configuration, and searching for the key that you've just added:

```{ .sh .copy }
nix config show | grep trusted-public-key
```

---


## The Tech Behind Imageless Kubernetes

> Source: `k8s/tech.md`

---
title: "Tech"
description: "The tech behind Imageless Kubernetes"
---

# The Tech Behind Imageless Kubernetes

Flox is a next-generation, language-agnostic package and environment manager.
With it you define "environments" that contain packages, environment variables, setup scripts, services, and more.
Every environment produces a lockfile when built so that anyone using Flox can reproduce the environment.
This means that the same environment works on your machine, your coworker's machine, in CI, and in production.

From a user's perspective, activating a Flox environment places the user into a shell that contains all of the packages, variables, etc defined in their environment.
Contrast this with a container that contains a filesystem image that has been imperatively built via a Dockerfile or some other means.

With Imageless Kubernetes you deploy pods that run commands inside of a Flox environment rather than a container instantiated from a container image.

## containerd-shim

Under the hood, Imageless Kubernetes works by wrapping `containerd-shim-runc-v2` to make Flox-specific modifications to the container config and filesystem.
The diagram below shows the high level overview of how Imageless Kubernetes works.

![containerd](../img/containerd.png)

Typically `containerd` produces a `config.json` describing the container's namespace requirements, mount points, etc.
This `config.json` is provided to a `containerd-shim` that then calls `runc` in order to create the container.
`runc` then creates and starts the container using the information in `config.json`.

With Imageless Kubernetes, `containerd-shim-flox-v2` intercepts the container configuration to prepare the container with everything needed to run the Flox environment.
The shim performs a number of operations to prepare the container's filesystem, including pulling the specified Flox environment to the node so that it can be mounted into the container.

The shim also modifies the container's command to run it in the context of the Flox environment rather than running the command directly.

---


## Upgrading

> Source: `k8s/install/upgrading.md`

---
title: "Upgrading"
description: "Upgrading Imageless Kubernetes"
---

This guide details how to perform upgrades on Flox and Imageless Kubernetes installed in a cluster.

## Amazon EKS

If a separate node group was created per the [install guidance][eks], then upgrading Flox and the runtime shim
can be accomplished by forcing replacement of the nodes in the cluster.

The configuration as given in the documentation will automatically install the latest version of Flox
and the runtime shim at node startup -- no other action is required.

## Self-managed

On self-managed clusters, both Flox and the runtime shim must be upgraded individually on each node.

For Flox, the [Install Flox][install-flox] page has details for each installation type on how to upgrade.

For the runtime shim, re-running the install command will perform the upgrade.
It can be done with:

```sh
flox activate -r flox/containerd-shim-flox-installer --trust
```

after which, all new pods will be created with the new shim version.

Existing Flox pods will only use the new version once they are restarted.

[eks]: ./eks.md
[install-flox]: ../../install-flox/install.md

---


---

# End of Documentation

This document was automatically generated from the official Flox documentation repository.
For the most current information, visit https://flox.dev/docs/
