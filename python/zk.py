#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pykeeper,HAZKInfo_pb2,yarn_server_resourcemanager_service_protos_pb2

class zk():
    def __init__(self):
        pykeeper.install_log_stream()

    def GetActiveNN(self,zkServer,path):
        try:
            client = pykeeper.ZooKeeper(zkServer)
            client.connect()
            ActiveNode =HAZKInfo_pb2.ActiveNodeInfo()
            ActiveNode.ParseFromString(client.get(path)[0])

            ActiveNamenode = ActiveNode.hostname.strip()
            print "ActiveNamenode : %s" % (ActiveNamenode)
            #return ActiveNamenode
        except:
            print "%s timeout" % zkServer
        finally:
            client.close()
    def GetActiveYarn(self,zkServer,yarn):
        try:
            client = pykeeper.ZooKeeper(zkServer)
            client.connect()
            path = '/yarn-leader-election/%s/ActiveBreadCrumb' % yarn
            ActiveRMInfo = yarn_server_resourcemanager_service_protos_pb2.ActiveRMInfoProto()
            ActiveRMInfo.ParseFromString(client.get(path)[0])
            ActiveRMID = ActiveRMInfo.rmId.strip()
            print "ActiveRMID : %s" % ActiveRMID
            # Yarn1
            if self.service == 'yarn1' and ActiveRMID == 'rm1':
                return "bj-dc-jn-001.tendcloud.com"
            elif self.service == 'yarn1' and ActiveRMID == 'rm2':
                return "bj-dc-jn-002.tendcloud.com"
        except:
            pass
        finally:
            client.close()
    def GetActiveHmaster(self):
        try:
            client = pykeeper.ZooKeeper(self.zkSvr)
            client.connect()
            hmaster = client.get(self.path)
            return hmaster
        except:
            pass
        finally:
            client.close()
class main():
    dchadoop301zk = "192.168.10.10:2181"
    znodePath = '/yhhadoop310001-ha/yhhadoop310001/ActiveBreadCrumb'
    zk().GetActiveNN(dchadoop301zk,znodePath)
    yarnNb='Yarn1'
    zk().GetActiveYarn(dchadoop301zk,yarnNb)
    
    
if __name__ == "__main__":
    main()
