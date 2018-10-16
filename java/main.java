import com.google.protobuf.InvalidProtocolBufferException;
import org.apache.zookeeper.KeeperException;
import org.talkingdata.hadoop.modules.ZookeeperTool;

import java.io.IOException;

/**
 *  Get Active Node from zookeeper
 */
public class main
{
    public static void main( String[] args )
    {
        String dchd310zk="172.10.1:2181";
        String namenodeparentznode= "/hadoop310-ha/hadoop310001/ActiveBreadCrumb";
        String yarn1parentznode = "/yarn-leader-election/Yarn1/ActiveBreadCrumb";
        ZookeeperTool zk = new ZookeeperTool();
        try {
            zk.getConnection(dchd310zk);
            String dcActiveNameNode = zk.getActiveNameNode(namenodeparentznode,true);
            System.out.println("dcActiveNameNode = " + dcActiveNameNode);
            String ActiveRMID = zk.getActiveYarn(yarn1parentznode);
            System.out.println("ActiveRMID =  " + ActiveRMID );
        } catch (KeeperException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (InvalidProtocolBufferException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
