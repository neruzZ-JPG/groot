data collect方案：

1. helm install
2. 正常跑1天
3. metrics_collect
4. helm uninstall & helm install
5. 修改配置
6. 跑1h
7. metrics_collect
8. helm uninstall