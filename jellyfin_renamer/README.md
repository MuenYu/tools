# jellyfin_renamer
jellyfin 官方命名格式见: [官方文档](https://jellyfin.org/docs/general/server/media/shows.html)

## 功能说明
1. 当前脚本仅用于 TV show
2. 需要手动对文件夹进行命名, 此脚本仅执行文件重命名
3. 请务必检查文件目录结构是否符合要求, 重命名依赖目录结构
4. 请务必保证剧集和字幕文件按照升序排列

## 使用方法
需要本机有 python 环境

```
python main.py {需要重命名的目录}
```

比如:
```
python main.py d:\樱花庄的宠物女孩
```