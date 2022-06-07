import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kotonohagetter", # 設定する名前
    version="0.0.1", # バージョン設定
    author="kyohei fujimori", # 名前
    author_email="ohnishi.rikito@gmail.com", # メアド変更
    description='A package for visualization of aggregate data of players in "Kotoha Tango"', # 説明文書書き換え
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/plumchloride/kotonohatango-getter", # GitHubURL
    project_urls={
        "Bug Tracker": "https://github.com/plumchloride/kotonohatango-getter", #GitHubURL
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['kotonohagetter'], # 設定するモジュール名
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    entry_points = {
        'console_scripts': [
            'kotonohagetter = kotonohagetter:main' # srcの中にある.pyの手前の文字
        ]
    },
)