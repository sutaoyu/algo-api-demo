#!/bin/bash

# 检查参数数量
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <old_name> <new_name>"
    exit 1
fi

OLD_NAME="$1"
NEW_NAME="$2"

# 定义需要修改的文件列表
FILES=("run_app.sh" "stop_app.sh" "gunicorn.py")

# 遍历每个文件并进行替换
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "Modifying $file..."
        sed -i "s/$OLD_NAME/$NEW_NAME/g" "$file"
        echo "Done."
    else
        echo "Warning: File $file not found, skipping..."
    fi
done

echo "Project name has been updated from $OLD_NAME to $NEW_NAME in all files."