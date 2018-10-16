import com.google.protobuf.InvalidProtocolBufferException;
import org.apache.hadoop.hdfs.server.namenode.ha.proto.HAZKInfoProtos;
import org.apache.zookeeper.*;
import java.io.IOException;
import java.util.List;
import static java.lang.System.out;
import static org.apache.hadoop.yarn.proto.YarnServerResourceManagerServiceProtos.*;
/**
 *  ZookeeperTool :
 *  获取Active Node 信息
 *
 */
public class ZookeeperTool {

    private static final int SESSION_TIMEOUT = 5000;
    private static ZooKeeper zk;

    public void getConnection(String zookeeper_address) throws IOException {
        zk = new ZooKeeper(zookeeper_address, SESSION_TIMEOUT, new Watcher() {
            @Override
            public void process(WatchedEvent watchedEvent) {
                System.out.println("");
                out.println("zookeeper service connection succeed ! ");
            }
        });

    }
    public  void getChildren (String desc_path) throws KeeperException, InterruptedException {
        List<String> children = zk.getChildren(desc_path,true);
        for (String path : children) {
            out.print(path+" ");
        }
    }
    public byte[] getData(String descPath) throws KeeperException, InterruptedException {
        byte [] data = zk.getData(descPath ,true,null);
        return data;
    }
    public void createFile (String filePath,String content ) throws KeeperException, InterruptedException {
        String c  = zk.create(filePath, content.getBytes(), ZooDefs.Ids.OPEN_ACL_UNSAFE, CreateMode.PERSISTENT);
        out.println( c + "Data write succeed");
    }

    public void setData (String filePath,String content ) throws KeeperException, InterruptedException {
        zk.setData(filePath,content.getBytes(),-1);
    }
    public void deleteData(String descPath) throws KeeperException, InterruptedException {
        zk.delete(descPath,-1);
    }
    public String getActiveNameNode(String descPath,boolean proto) throws KeeperException, InterruptedException, InvalidProtocolBufferException {
        byte [] data = zk.getData(descPath ,true,null);
        HAZKInfoProtos.ActiveNodeInfo nodeInfo = HAZKInfoProtos.ActiveNodeInfo.parseFrom(data);
        String protodata = nodeInfo.getHostname();
        return protodata;
    }
    public String getActiveYarn(String descPath) throws InvalidProtocolBufferException, KeeperException, InterruptedException {
        byte [] data = zk.getData(descPath ,true,null);
        return (ActiveRMInfoProto.parseFrom(data).getRmId());
    }
}
