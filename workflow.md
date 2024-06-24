start_program(){
    Multi-Threading{
    Thread1 : Start WebsocketServer  
    Thread2 : initiate_node {
        store Host IPv4Address Information to Node Database
        (Credential Initiated ? [Yes] -> next , [No] -> Generate Public Key and Private Key Then Store to Node Database )
        Start Synchronization from Others Node
        Choose Menu : 
        1. Create Transaction
        2. Get Transacation History
        3. Get Local Block-Chain Data
        0. Return to main Menu
    }
    Thread3 : Start WebsocketClient
    }
}

create_transaction{
    Enter the Receiver Address
    Enter the Receiver ID
    Verify the Local BlockChain , if Valid then Next step, if invalid Synchronize first than next step
    Mine The Block
    add The Block to local BlockChain Data
    Broadcast the Block with WebSocket Server
}