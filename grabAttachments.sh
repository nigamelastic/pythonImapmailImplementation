#!/bin/bash
mkdir attachments
python3 grabAllAttachments.py
mkdir csvExtr
mv attachments/*.csv csvExtr/
for files in attachments/*.zip; do unzip -p "${files}" > "${files}-.csv"; done
mv attachments/*.csv csvExtr/

