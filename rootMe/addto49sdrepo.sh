#!/bin/bash
rm -rf /root/49sd_main_repo/.git
cd /root/49sd_main_repo
git init
unzip -o -d /root/49sd_main_repo /home/49sd/repos/*
git add .
git commit --allow-empty -m "49sd's Commit!!!"
rm -f /home/49sd/repos/*
