# qubes-app-youtube-dl
Wraps awesome [youtube-dl-gui](https://github.com/MrS0m30n3/youtube-dl-gui), a front-end GUI for [youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html) written in wxPython. 

By now, [youtube-dl-gui](https://github.com/MrS0m30n3/youtube-dl-gui) is not a strict requirement, altough it is highly recommended for more interaction, more options and asynchronous download system.
In the case it is not installed, an old-zenity-handwritten GUI is presented as a fallback.

For more informations about [youtube-dl-gui-wrapper](#youtube-dl-gui-wrapper).

# Why?
The main design is to split the vm which handle downloads and the one which actually reproduce the media content. 

Here it needs two vms:
- youtube-dl-vm (disposable or not): contains the youtube-dl binary which actually download everything and has full or limited network access.
- media-vm: acts like a vault vm, but for media. No network access yada yada. After the `youtube-dl-vm` do it's operations, will move downloaded data to some vm, which in fact should be this one.

**You are not protected against malicious downloaded video/audio files.**

**You are not protected against hipotetically bug in youtube-dl which further compromises the download operation which could make an attacker maliciously tamper video/audio files.**

You are protected against allowing malicious video/audio files accessing network directly.

So, this script is just an automation to make our life easier, but off course that is something you could (kind of) do easily by yourself.

# Youtube-Dl-GUI Wrapper
The [youtube-dl-gui](https://github.com/MrS0m30n3/youtube-dl-gui) appplication does a nice job creating a front-end interface for [youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html). As already stated, it is recommended instead of default interface based on zenity. 

So how it works? The youtube-dl-gui app is started, the user add urls, downloads it and when the app is closed we (kind of) gently ask the app all the video/audio files the user had downloaded with success. Now it is easy, we just copy it to another vm.

# Getting Started
## Requirements:
- [python-2.7+](https://www.python.org/downloads/)
- [youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html)
- one of the following should be installed as front-end GUI:
    - [youtube-dl-gui](https://github.com/MrS0m30n3/youtube-dl-gui) (recommended)
    - [zenity](https://help.gnome.org/users/zenity/3.32/intro.html.en) (generally already installed by your OS)

## Download and Verify
There are two methods to download and verify. The first assumes you are a github user with an active account. The later uses a source distribution archive, which does not require a github account. The both ways should result in the same thing.

Wait...before proceed make sure you get author's public key:
```bash
$ gpg --keyserver keys.gnupg.net --recv-keys 0xB677080945DF2D38C7C5F15F80AB0F5FDECFB4A9
```
as Qubes itself always confirm, [distrust the infrastructure](https://www.qubes-os.org/faq/#what-does-it-mean-to-distrust-the-infrastructure), you may also check the public key from another keyserver, from github [gpg keys api](https://developer.github.com/v3/users/gpg_keys/#list-gpg-keys-for-a-user), etc...

### Cloning
- clone the repo in some domU with network access:
```bash
$ git clone git@github.com:yanmarques/qubes-app-youtube-dl.git
```

- verify repo tag, inside cloned directory:
```bash
$ git tag -v v0.1
```

### Source archive
- download the source archive using your favorite download manager:
```bash
$ wget https://github.com/yanmarques/qubes-app-youtube-dl/releases/download/v0.2/qubes-app-youtube-dl-0.2.tar.gz
```

- download the source archive signature for further checking the archive integrity and confidentiality:
```bash
$ wget https://github.com/yanmarques/qubes-app-youtube-dl/releases/download/v0.2/qubes-app-youtube-dl-0.2.tar.gz.sig
```

- verify it now:
```bash
$ git --verify qubes-app-youtube-dl-0.2.tar.gz.sig qubes-app-youtube-dl-0.2.tar.gz
```

From the both methods, after verifying, one should see a `Good signature`, otherwhise go back and repeat above steps or search for help.

## Install
### Dom0 (Optional)
One may want to simplify copying downloaded content to the same media vm. If this is true, change the content of `qubes.Filecopy.policy` where:
- `your-youtube-dl-vm`: the base youtube-dl appvm, by default this vm must be template for disposable vms, but you may remove the `$disp:` part to avoid this behavior.
- `your-media-vm`: the media vm to move content for.

Now append the contents of `qubes.Filecopy.policy` to dom0 at `/etc/qubes-rpc/policy/qubes.Filecopy`.

### YoutubeDl VM
The easiest way to install it by now is from source.

One may choose a templatevm to use as base for your youtube-dl appvm, and that one will be called as `base templatevm` by now.

- from your `domU`, copy the downloaded and verified project to the `base templatevm`:
```bash
$ qvm-copy DOWNLOAD-AND-VERIFIFIED-PROJECT-DIRECTORY
```

- from your `base templatevm`, inside `QubesIncoming` copied directory, do as **root**:
```bash
$ python setup.py install
```

- in your `base templatevm` settings, refresh your applications, and you should see it discovered something like `Download Youtube Songs/Videos`
- now shutdown your `base templatevm` and create your youtube-dl-vm with this templatevm as template

# License
See [here](/LICENSE)