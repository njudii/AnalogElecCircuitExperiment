# 模电实验LaTeX模板

对于匡院物理方向的学生来说，``模电打字实验``和``近代排版实验``是两门比较鸡肋的课程。在课程负担较重的大三下还要应付实验报告是一件烦心事。这个模板旨在把匡院学生从ben无意义的实验报告中解放出来，有更多精力去钻研和思考实验本身。

---

**注意：** 不可以原封不动直接用，需要自己检查、修改内容。为了不被查水表，思考题的解答已经被去除(但是...)。

---

文字来源：实验网站、教材。

特别鸣谢circuitikz电路图的作者：[WilliamXu](https://github.com/WilliamXu980906)。

tex文件：[Young](https://github.com/github-young)。

附一个实用工具：[能生成LaTeX表格的网站](https://www.tablesgenerator.com/)

---

Heads up!

 - 如果需要LaTeX相关的帮助，请查看 [软件教学系列的文章](https://itxia.github.io/categories/%E8%BD%AF%E4%BB%B6%E6%95%99%E5%AD%A6%E7%B3%BB%E5%88%97/)。

 - 中文路径的问题：vscode+LaTeX workshop编译含有中文路径的文件会有问题，解决办法有两个：
   1. 用sublime+LaTeX Tools
   2. 修改vscode的settings.json的下列段落中的``DOC``为``DOCFILE``，修改后的段落如下（此方法来自[这个项目的FAQ](https://github.com/James-Yu/LaTeX-Workshop)）：
   
   ```
   "latex-workshop.latex.tools": [
    {
      "name": "latexmk",
      "command": "latexmk",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-shell-escape",
        "-pdf",
        "%DOCFILE%"
      ]
    },
    {
      "name": "xelatex",
      "command": "xelatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-shell-escape",
        "-pdf",
        "%DOCFILE%"
      ]
    },
    {
      "name": "bibtex",
      "command": "bibtex",
      "args": [
        "%DOCFILE%"
      ]
    }
   ],
   ```
