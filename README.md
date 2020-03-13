# 麦课 (mycourse.cn) 自动学习, 测试

# 使用方法

## 整合题库(可选)

使用任意数目的进行过测试的帐号, 在浏览器中登录 `weiban.mycourse.cn`, 将每个 `/reviewPaper.do` 的响应保存为 `json` 类型的文件, 都置于 `QuestionBanks` 文件夹中, 运行 `loadQuestionBanks.py`, 再将文件夹中的文件删除

## 自动学习, 测试

在浏览器中登录 `weiban.mycourse.cn`, 将 `configTemplate.yaml` 文件更名为 `config.yaml`, 并配置, 运行 `learnAndExam.py`, 根据提示操作

# 免责声明

下载, 使用脚本时均视为已经仔细阅读并完全同意以下条款:

- 脚本仅供个人学习与交流使用, 严禁用于商业以及不良用途
- 使用本脚本所存在的风险将完全由其本人承担, 脚本作者不承担任何责任
- 本声明未涉及的问题请参见国家有关法律法规, 当本声明与国家有关法律法规冲突时, 以国家法律法规为准