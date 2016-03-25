#Starting AdminServer through NodeManager
nmConnect('weblogic','welcome1',domainName='base_domain',port='5556',host='localhost')
nmStart('AdminServer')
nmDisconnect()

connect('weblogic','welcome1','t3://localhost:7001')

# Adding user to default security realm
print "************************ Adding Administrator user in default security realm ****************************"
serverConfig()
cd('/')
realm=cmo.getSecurityConfiguration().getDefaultRealm()
atnr=realm.lookupAuthenticationProvider('DefaultAuthenticator')
atnr.createUser('administrator','administrator123','Medrec Admin')

edit()

# Creating Machine in base_domain
print "************************ Creating machine in base_domain ****************************"
startEdit()
cd('/')
cmo.createUnixMachine('machine')
cd('/Machines/machine/NodeManager/machine')
cmo.setNMType('SSL')
cmo.setListenAddress('localhost')
cmo.setListenPort(5556)
cmo.setDebugEnabled(false)
activate()

#Creating Dynamic Cluster in base_domain
print "************************ Creating dynamic cluster app-cluster ****************************"
startEdit()
cd('/')
cmo.createServerTemplate('app-cluster-Template')
cd('/ServerTemplates/app-cluster-Template')
cmo.setListenPort(7100)
cd('/ServerTemplates/app-cluster-Template/SSL/app-cluster-Template')
cmo.setListenPort(8100)
cd('/ServerTemplates/app-cluster-Template')
cmo.setMachine(getMBean('/Machines/machine'))
cd('/')
cmo.createCluster('app-cluster')
cd('/Clusters/app-cluster')
cmo.setClusterMessagingMode('unicast')
cd('/ServerTemplates/app-cluster-Template')
cmo.setCluster(getMBean('/Clusters/app-cluster'))
cd('/Clusters/app-cluster/DynamicServers/app-cluster')
cmo.setServerTemplate(getMBean('/ServerTemplates/app-cluster-Template'))
cmo.setDynamicClusterSize(2)
cmo.setMaxDynamicClusterSize(8)
cmo.setCalculatedListenPorts(true)
cmo.setCalculatedMachineNames(false)
cmo.setCalculatedListenPorts(true)
cmo.setServerNamePrefix('app-cluster-')
activate()

disconnect()




# Connecting to Admin Server to create the Partitions
connect('weblogic','welcome1','t3://localhost:7001')
print "************************ Starting app-cluster ****************************"
start('app-cluster','Cluster')

edit()

# Creating Virtual Target and Domain partition dp1
print "************************ Creating Virtual target VT-Medrec-1 for dp1  ****************************"
startEdit()
cd('/')
cmo.createVirtualTarget('VT-Medrec-1')
cd('/VirtualTargets/VT-Medrec-1')
cmo.setHostNames(array(["localhost"],java.lang.String))
cmo.setUriPrefix('/dp1')
set('Targets',jarray.array([ObjectName('com.bea:Name=app-cluster,Type=Cluster')], ObjectName))
activate()
print "************************ Creating domain partition dp1 in base_domain ****************************"
startEdit()
cd('/')
cmo.createPartition('dp1')
cd('/Partitions/dp1/SystemFileSystem/dp1')
cmo.setRoot('/u01/wins/wls1221/user_projects/domains/base_domain/partitions/dp1/system')
cmo.setCreateOnDemand(true)
cmo.setPreserved(true)
cd('/Partitions/dp1')
set('AvailableTargets',jarray.array([ObjectName('com.bea:Name=VT-Medrec-1,Type=VirtualTarget')], ObjectName))
set('DefaultTargets',jarray.array([ObjectName('com.bea:Name=VT-Medrec-1,Type=VirtualTarget')], ObjectName))
activate()
print "************************ Creating Resource Group app1RG in dp1 partition ****************************"
startEdit()
cmo.createResourceGroup('app1RG')
cd('/Partitions/dp1/ResourceGroups/app1RG')
cmo.setUseDefaultTarget(false)
set('Targets',jarray.array([ObjectName('com.bea:Name=VT-Medrec-1,Type=VirtualTarget')], ObjectName))
activate()
print "************************ Creating JDBC datasource in app1RG resource group ****************************"
startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG')
cmo.createJDBCSystemResource('MedRec1GlobalDataSourceXA')
cd('/Partitions/dp1/ResourceGroups/app1RG/JDBCSystemResources/MedRec1GlobalDataSourceXA/JDBCResource/MedRec1GlobalDataSourceXA')
cmo.setName('MedRec1GlobalDataSourceXA')
cd('/Partitions/dp1/ResourceGroups/app1RG/JDBCSystemResources/MedRec1GlobalDataSourceXA/JDBCResource/MedRec1GlobalDataSourceXA/JDBCDataSourceParams/MedRec1GlobalDataSourceXA')
set('JNDINames',jarray.array([String('jdbc/MedRecGlobalDataSourceXA')], String))
cd('/Partitions/dp1/ResourceGroups/app1RG/JDBCSystemResources/MedRec1GlobalDataSourceXA/JDBCResource/MedRec1GlobalDataSourceXA')
cmo.setDatasourceType('GENERIC')
cd('/Partitions/dp1/ResourceGroups/app1RG/JDBCSystemResources/MedRec1GlobalDataSourceXA/JDBCResource/MedRec1GlobalDataSourceXA/JDBCDriverParams/MedRec1GlobalDataSourceXA')
cmo.setUrl('jdbc:oracle:thin:@//localhost:1521/pdborcl')
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
cmo.setPassword('medrec1')
cd('/Partitions/dp1/ResourceGroups/app1RG/JDBCSystemResources/MedRec1GlobalDataSourceXA/JDBCResource/MedRec1GlobalDataSourceXA/JDBCConnectionPoolParams/MedRec1GlobalDataSourceXA')
cmo.setTestTableName('SQL ISVALID\r\n\r\n')
cd('/Partitions/dp1/ResourceGroups/app1RG/JDBCSystemResources/MedRec1GlobalDataSourceXA/JDBCResource/MedRec1GlobalDataSourceXA/JDBCDriverParams/MedRec1GlobalDataSourceXA/Properties/MedRec1GlobalDataSourceXA')
cmo.createProperty('user')
cd('/Partitions/dp1/ResourceGroups/app1RG/JDBCSystemResources/MedRec1GlobalDataSourceXA/JDBCResource/MedRec1GlobalDataSourceXA/JDBCDriverParams/MedRec1GlobalDataSourceXA/Properties/MedRec1GlobalDataSourceXA/Properties/user')
cmo.setValue('medrec1')
cd('/Partitions/dp1/ResourceGroups/app1RG/JDBCSystemResources/MedRec1GlobalDataSourceXA/JDBCResource/MedRec1GlobalDataSourceXA/JDBCDataSourceParams/MedRec1GlobalDataSourceXA')
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')
activate()
print "************************ Creating Mail Session in app1RG resource group ****************************"
startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG')
cmo.createMailSession('MedRec1MailSession')
cd('/Partitions/dp1/ResourceGroups/app1RG/MailSessions/MedRec1MailSession')
cmo.setJNDIName('mail/MedRecMailSession')
activate()
print "************************ Creating file-store in app1RG resource group ****************************"
startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG')
cmo.createFileStore('MedRec1-fs')
activate()
print "************************ Creating JMS Server in app1RG resource group  ****************************"
startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG')
cmo.createJMSServer('MedRec1JMSServer')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSServers/MedRec1JMSServer')
cmo.setPersistentStore(getMBean('/Partitions/dp1/ResourceGroups/app1RG/FileStores/MedRec1-fs'))
activate()

print "************************ Creating JMS Module in app1RG resource group ****************************"
startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG')
cmo.createJMSSystemResource('MedRecModule')
activate()
print "************************ Creating Subdeployment in app1RG resource group ****************************"
startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule')
cmo.createSubDeployment('MedRec1JMS ')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/SubDeployments/MedRec1JMS')
set('Targets',jarray.array([ObjectName('com.bea:Name=MedRec1JMSServer,Type=JMSServer,Partition=dp1,ResourceGroup=app1RG')], ObjectName))
activate()
print "************************ Creating connection factory in app1RG resource group ****************************"
startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule')
cmo.createConnectionFactory('MedRec1ConnectionFactory')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec1ConnectionFactory')
cmo.setJNDIName('com.oracle.medrec.jms.connectionFactory')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec1ConnectionFactory/SecurityParams/MedRec1ConnectionFactory')
cmo.setAttachJMSXUserId(false)
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec1ConnectionFactory/ClientParams/MedRec1ConnectionFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec1ConnectionFactory/TransactionParams/MedRec1ConnectionFactory')
cmo.setXAConnectionFactoryEnabled(true)
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec1ConnectionFactory')
cmo.setDefaultTargetingEnabled(true)
activate()
print "************************ Creating Distributed uniform JMS Queue in app1RG resource group  ****************************"
startEdit()
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule')
cmo.createUniformDistributedQueue('PatientNotificationQueue')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/UniformDistributedQueues/PatientNotificationQueue')
cmo.setJNDIName('com.oracle.medrec.jms.PatientNotificationQueue')
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/SubDeployments/MedRec1JMS')
set('Targets',jarray.array([ObjectName('com.bea:Name=MedRec1JMSServer,Type=JMSServer,Partition=dp1,ResourceGroup=app1RG')], ObjectName))
cd('/Partitions/dp1/ResourceGroups/app1RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/UniformDistributedQueues/PatientNotificationQueue')
cmo.setSubDeploymentName('MedRec1JMS')
activate()
print "************************ Deploying medrec applications in app1RG resource group ****************************"
startEdit()
deploy(appName='medrec', partition='dp1', resourceGroup='app1RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab2/medrec.ear')
deploy(appName='physician', partition='dp1', resourceGroup='app1RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab2/physician.ear')
deploy(appName='chat', partition='dp1', resourceGroup='app1RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab2/chat.war')
activate()
print "************************ Starting domain partition dp1 ****************************"
startEdit()
cd('/')
partitionBean=cmo.lookupPartition('dp1')
startPartitionWait(partitionBean)
activate()

#Medrec in Domain Partition dp2
print "************************ Creating Virtual Target for domain partition dp2 ****************************"
startEdit()
cd('/')
cmo.createVirtualTarget('VT-Medrec-2')
cd('/VirtualTargets/VT-Medrec-2')
cmo.setHostNames(array(["localhost"],java.lang.String))
cmo.setUriPrefix('/dp2')
set('Targets',jarray.array([ObjectName('com.bea:Name=app-cluster,Type=Cluster')], ObjectName))
activate()
print "************************ Creating Domain Partition dp2 in base_domain ****************************"
startEdit()
cd('/')
cmo.createPartition('dp2')
cd('/Partitions/dp2/SystemFileSystem/dp2')
cmo.setRoot('/u01/wins/wls1221/user_projects/domains/base_domain/partitions/dp2/system')
cmo.setCreateOnDemand(true)
cmo.setPreserved(true)
cd('/Partitions/dp2')
set('AvailableTargets',jarray.array([ObjectName('com.bea:Name=VT-Medrec-2,Type=VirtualTarget')], ObjectName))
set('DefaultTargets',jarray.array([ObjectName('com.bea:Name=VT-Medrec-2,Type=VirtualTarget')], ObjectName))
activate()
print "************************ Creating app2RG resource group in dp2 ****************************"
startEdit()
cmo.createResourceGroup('app2RG')
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.setUseDefaultTarget(false)
set('Targets',jarray.array([ObjectName('com.bea:Name=VT-Medrec-2,Type=VirtualTarget')], ObjectName))
activate()
print "************************ Creating JDBC datasource in app2RG resource group  ****************************"
startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.createJDBCSystemResource('MedRec2GlobalDataSourceXA')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA')
cmo.setName('MedRec2GlobalDataSourceXA')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCDataSourceParams/MedRec2GlobalDataSourceXA')
set('JNDINames',jarray.array([String('jdbc/MedRecGlobalDataSourceXA')], String))
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA')
cmo.setDatasourceType('GENERIC')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCDriverParams/MedRec2GlobalDataSourceXA')
cmo.setUrl('jdbc:oracle:thin:@//localhost:1521/pdb2')
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
cmo.setPassword('medrec2')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCConnectionPoolParams/MedRec2GlobalDataSourceXA')
cmo.setTestTableName('SQL ISVALID\r\n\r\n')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCDriverParams/MedRec2GlobalDataSourceXA/Properties/MedRec2GlobalDataSourceXA')
cmo.createProperty('user')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCDriverParams/MedRec2GlobalDataSourceXA/Properties/MedRec2GlobalDataSourceXA/Properties/user')
cmo.setValue('medrec2')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCDataSourceParams/MedRec2GlobalDataSourceXA')
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')
activate()
print "************************ Creating Mail Session in app2RG resource group ****************************"
startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.createMailSession('MedRec2MailSession')
cd('/Partitions/dp2/ResourceGroups/app2RG/MailSessions/MedRec2MailSession')
cmo.setJNDIName('mail/MedRecMailSession')
activate()
print "************************ Creating File Store in app2RG resource group ****************************"
startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.createFileStore('MedRec2-fs')
activate()
print "************************ Creating JMS Server in app2RG resource group ****************************"
startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.createJMSServer('MedRec2JMSServer')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSServers/MedRec2JMSServer')
cmo.setPersistentStore(getMBean('/Partitions/dp2/ResourceGroups/app2RG/FileStores/MedRec2-fs'))
activate()

print "************************ Creating JMS Module in app2Rg resource group ****************************"
startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.createJMSSystemResource('MedRecModule')
activate()
print "************************ Creating Subdeployment in app2RG resource group ****************************"
startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule')
cmo.createSubDeployment('MedRec2JMS ')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/SubDeployments/MedRec2JMS')
set('Targets',jarray.array([ObjectName('com.bea:Name=MedRec2JMSServer,Type=JMSServer,Partition=dp2,ResourceGroup=app2RG')], ObjectName))
activate()
print "************************ Creating Connection Factory in app2RG resource group ****************************"
startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule')
cmo.createConnectionFactory('MedRec2ConnectionFactory')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec2ConnectionFactory')
cmo.setJNDIName('com.oracle.medrec.jms.connectionFactory')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec2ConnectionFactory/SecurityParams/MedRec2ConnectionFactory')
cmo.setAttachJMSXUserId(false)
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec2ConnectionFactory/ClientParams/MedRec2ConnectionFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec2ConnectionFactory/TransactionParams/MedRec2ConnectionFactory')
cmo.setXAConnectionFactoryEnabled(true)
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec2ConnectionFactory')
cmo.setDefaultTargetingEnabled(true)
activate()
print "************************ Creating Uniform Distributed JMS Queue in app2RG resource group  ****************************"
startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule')
cmo.createUniformDistributedQueue('PatientNotificationQueue')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/UniformDistributedQueues/PatientNotificationQueue')
cmo.setJNDIName('com.oracle.medrec.jms.PatientNotificationQueue')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/SubDeployments/MedRec2JMS')
set('Targets',jarray.array([ObjectName('com.bea:Name=MedRec2JMSServer,Type=JMSServer,Partition=dp2,ResourceGroup=app2RG')], ObjectName))
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/UniformDistributedQueues/PatientNotificationQueue')
cmo.setSubDeploymentName('MedRec2JMS')
activate()
print "************************ Deploy Medrec applications in app2RG resource group ****************************"
startEdit()
deploy(appName='medrec', partition='dp2', resourceGroup='app2RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab2/medrec.ear')
deploy(appName='physician', partition='dp2', resourceGroup='app2RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab2/physician.ear')
deploy(appName='chat', partition='dp2', resourceGroup='app2RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab2/chat.war')
activate()
print "************************ Starting domain partition in dp2 ****************************"
startEdit()
cd('/')
partitionBean=cmo.lookupPartition('dp2')
startPartitionWait(partitionBean)
activate()

disconnect()


