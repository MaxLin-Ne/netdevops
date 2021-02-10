银狐DevNet系列会持续将网络运维工作中python的应用进行场景化的分享，因为每个单独的模块网上都有详细的教学，这里就不深入讲解模块基础了，内容主要以思路和示例为主，并将碰到的问题汇总提出注意事项。

主要是因为网络工程师和网络运维工作者编程基础不强，加上网上对于这个领域的python资料又少，传统的分享方式（每个章节仅单纯分享一个知识点）对于很多网工来说各个知识点相对独立且割裂的，很难进行一个知识的融合，现实工作中也很难直接应用，大家学习的难度就会很大，也会导致大部分人刚入门就放弃。所以我将这些内容进行场景化，根据特定场景由浅入深不断优化，从而带出更多知识点，希望对大家有所帮助。

这些分享都是我本人真实的学习路径，一方面是帮助自己梳理网络自动化相关知识，另一方面也希望可以通过分享我微不足道的学习过程和实战经验，帮助更多想要了解NetDevOps而苦于没有资料和环境被劝退的人，进而找到同行之人互相交流、互相提升。

场景01：使用协程gevent，结合Netmiko批量抓取上百台设备网络配置并存入本地，现实运维场景中抓取200台设备需要的时间不会超过20秒。
