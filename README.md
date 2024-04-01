# Building a Distributed Key - Value Store with etcd

## Introduction

Etcd is an open-source distributed key value store that provides strong consistency and survivability of data. Its major characteristics :

- **Distributed Key-Value Store**: Etcd is an open-source distributed key-value store.
- **Strong Consistency**: It provides strong consistency guarantees, ensuring that data is always up-to-date and consistent across the cluster.
- **High Availability**: Etcd's distributed architecture ensures high availability by replicating data across multiple nodes. This ensures that the system remains operational even if some nodes fail.
- **Survivability**: It can survive network partitions and node failures, ensuring that data remains accessible and consistent under adverse conditions.
- **Use Cases**: Etcd is suitable for building highly available applications requiring data integrity and availability, such as service discovery, configuration management, distributed locking, and coordination among distributed systems.
- **Simple API**: It offers a simple and efficient API for storing, retrieving, and managing key-value pairs, abstracting away the complexities of distributed systems.
- **Watch Functionality**: Etcd supports watch functionality, enabling real-time notification of changes to data, making it suitable for building reactive and event-driven systems.
- **Resilient Architecture**: Etcd empowers developers to architect resilient and scalable distributed applications with ease, ensuring data consistency and availability across their infrastructure.

## Setting up Single Node Cluster

1. Launch etcd server :

   ```bash
    etcd
    {"level":"info","ts":"2021-09-17T09:19:32.783-0400","caller":"etcdmain/etcd.go:72","msg":... }
    ⋮
   ```

2. A single node cluster is setup , refer https://etcd.io/docs/v3.5/quickstart/ .

##
