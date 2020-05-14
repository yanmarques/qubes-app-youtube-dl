# qubes-app-youtube-dl
Wrap awesome [youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html) to help running it inside a vm without touching the terminal.

# Why?
The main design is to split the vm which handle downloads and the one which actually reproduce the media content. 

Here it needs two vms:
- youtube-dl-vm (disposable or not): contains the youtube-dl binary which actually download everything and has full or limited network access.
- media-vm: acts like a vault vm, but for media. No network access yada yada. After the `youtube-dl-vm` do it's operations, will move downloaded data to some vm, which in fact should be this one.

**You are not protected against malicious downloaded video/audio files.**

**You are not protected against hipotetically bug in youtube-dl which further compromises the download operation which could make an attacker maliciously tamper video/audio files.**

You are protected against allowing malicious video/audio files accessing network directly.

So, this script is just an automation to make our life easier, but off course that is something you could (kind of) do easily by yourself.

# Getting Started
## Download
- clone the repo in some domU with network access:
```bash
$ git clone git@github.com:yanmarques/qubes-usb3to2-service-dom0.git
```

- check gpg signature, first one must get the public key:
```bash
$ gpg2 --keyserver keys.gnupg.net --recv-keys 0xB677080945DF2D38C7C5F15F80AB0F5FDECFB4A9
```
as Qubes itself always confirm, [distrust the infrastructure](https://www.qubes-os.org/faq/#what-does-it-mean-to-distrust-the-infrastructure), you may also check the public key from another keyserver, from github [gpg keys api](https://developer.github.com/v3/users/gpg_keys/#list-gpg-keys-for-a-user), etc...

- verify repo tag, inside cloned directory:
```bash
$ git tag -v v0.1
```

one should see a `Good signature`, otherwhise go back and repeat above steps or search for help.


## Install
### Dom0 (Optional)
One may want to simplify copying downloaded content to the same media vm. If this is true, change the content of `qubes.Filecopy.policy` where:
- `your-youtube-dl-vm`: the base youtube-dl appvm, by default this vm must be template for disposable vms, but you may remove the `$disp:` part to avoid this behavior.
- `your-media-vm`: the media vm to move content for.

Now append the contents of `qubes.Filecopy.policy` to dom0 at `/etc/qubes-rpc/policy/qubes.Filecopy`.

### YoutubeDl VM
- choose a templatevm to use as base for your youtube-dl appvm, and make sure to install above packages:
    - youtube-dl (either by a package manager, pip, or the binary downloaded from their [website](https://ytdl-org.github.io/youtube-dl/download.html) since it is easily found from `PATH` env)
    - zenity (generally already installed by the OSes)

- from your `domU`, copy `qubes.YoutubeDl` and `youtube-dl-vm` to the `base templatevm`:
```bash
$ cd qubes-app-youtube-dl-master && qvm-copy qubes.YoutubeDl youtube-dl-vm
```

- from your `base templatevm`, inside `QubesIncoming` copied directory, do as **root**:
    - copy `qubes-youtube-dl` to `/usr/bin/`, make sure it is executable by everyone and owned by root:
    ```bash
    $ chmod 755 qubes-youtube-dl
    $ chown root:root qubes-youtube-dl
    $ cp qubes-youtube-dl /usr/bin/
    ```
    - copy desktop entries inside `youtube-dl-vm` to `/usr/share/applications`:
    ```bash
    $ chmod 644 youtube-dl-vm/*.desktop
    $ chown root:root youtube-dl-vm/*.desktop
    $ cp youtube-dl-vm/*.desktop /usr/share/applications/
    ```

- in your `base templatevm` settings, refresh your applications, and you should see it discovered something like `Download Youtube Songs/Videos`
- now shutdown your `base templatevm` and create your youtube-dl-vm with this templatevm as template

# License
See [here](/LICENSE)