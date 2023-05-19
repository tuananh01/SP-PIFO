from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

# Network general options
net.setLogLevel('info')
net.enableCli()

# Network definition
net.addP4Switch('s1', cli_input='sw_commands/s1_direct_commands.txt')
net.addP4Switch('s2', cli_input='sw_commands/s2_direct_commands.txt')
net.addP4Switch('s3', cli_input='sw_commands/s3_direct_commands.txt')
net.setP4SourceAll('sp-pifo.p4')

net.addHost('h1')
net.addHost('h11')
net.addHost('h10')
net.addHost('h2')
net.addHost('h22')
net.addHost('h3')
net.addHost('h33')

net.addLink('h1', 's1')
net.addLink('h11', 's1')
net.addLink('h10', 's1')
net.addLink('s1', 's2', bw=1)
net.addLink('h2', 's2')
net.addLink('h22', 's2')
net.addLink('s2', 's3', bw=1)
net.addLink('h3', 's3')
net.addLink('h33', 's3')


# Assignment strategy
net.mixed()

# Nodes general options
net.enablePcapDumpAll()
net.enableLogAll()

# Start the network
net.startNetwork()
