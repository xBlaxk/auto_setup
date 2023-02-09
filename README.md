# AUTO_SETUP

## DISCLAIMER
This may be all its lifespan in WIP this is because is totally intended to be made for pesonal use following my own configuration and desires.

If you thing this project may have a future and have an idea that can be usefull or any kind of code optimization don't doubt about pull request or if you want to make your own version you can fork this repo.

Thanks for readin.

## Description
this is project started thinking about solving a task I made manually really often "Download, Install and Setup my development enviorement".

Every time I format my computer or maybe just get a new laptop from my work I want to keep using the exact same dev enviroments in every single device, things like making sure I'm using "Z-Shell" as my main shell, have in it an installed theme, use the correct font, in the case of using windows install the WSL with the correct version of linux that I want to use, etc.

So this is what I'm gonan do, make a scrip for every single OS that will setup the configuration

## List of settings
- Fonts
  - Download .zip
  - Uncompress
  - Install .ttf|.otf
- Shell
  - Windows
    - `Git`
    - `Vim`
      - Import custom `.vim` config file
    - `NVM`
      - Download `NodeJS LTS` version
      - Set `LTS` as default `NodeJS` version
    - Set `PowerShell` as main bash
    - Setup `Oh My Posh`
      - Download
      - Install
      - Set Theme
  - Linux/Unix
    - `Git`
    - `Vim`
      - Import custom `.vim` config file
    - `NVM`
      - Download `NodeJS LTS` version
      - Set `LTS` as default `NodeJS` version
    - Set `Z-Shell` as main bash
    - Install `Oh My Zsh`
      - Download
      - Install
      - Change Theme
        - Set `powershell10k` as theme
        - Import custom `.p10k` config file
        - Import custom color scheme
  - Software
    - `VSCode`
      - Add `code` bash alias to open `VScode`
    - `Notion`
    - `OBS Studio`
    - `Discord`