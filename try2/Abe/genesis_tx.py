# Copyright(C) 2013 by Abe developers.

# genesis_tx.py: known transactions unavailable through RPC for
# historical reasons: https://bitcointalk.org/index.php?topic=119530.0

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

def get(tx_hash_hex):
    """
    Given the hexadecimal hash of the genesis transaction (as shown
    by, e.g., "bitcoind getblock 0") return the hexadecimal raw
    transaction.  This works around a Bitcoind limitation described at
    https://bitcointalk.org/index.php?topic=119530.0
    """

    # Main Bitcoin chain:
    if tx_hash_hex == "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b":
        return "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000"

    # NovaCoin:
    if tx_hash_hex == "4cb33b3b6a861dcbc685d3e614a9cafb945738d6833f182855679f2fad02057b":
        return "01000000398e1151010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d020f274468747470733a2f2f626974636f696e74616c6b2e6f72672f696e6465782e7068703f746f7069633d3133343137392e6d736731353032313936236d736731353032313936ffffffff0100000000000000000000000000"

    # CryptoCash / CashCoin:
    if tx_hash_hex == "c7e715851ef2eebd4a881c48f0d6140e187d8e8f417eaacb6c6e7ed6c462dbde":
        return "010000006eb7dc52010000000000000000000000000000000000000000000000000000000000000000ffffffff7604ffff001d020f274c6c4a616e2032302c20323031342031323a3430616d204544542e204e65776567672074656173657220737567676573747320746865205553206f6e6c696e652072657461696c206769616e74206d617920626567696e20616363657074696e6720626974636f696e20736f6f6effffffff0100000000000000000000000000"

    # Hirocoin
    if tx_hash_hex == "b0019d92bc054f7418960c91e252e7d24c77719c7a30128c5f6a827c73095d2a":
        return "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4f04ffff001d0104474a6170616e546f6461792031332f4d61722f323031342057617973206579656420746f206d616b6520706c616e65732065617369657220746f2066696e6420696e206f6365616effffffff0100902f50090000004341040184710fa689ad5023690c80f3a49c8f13f8d45b8c857fbcbc8bc4a8e4d3eb4b10f4d4604fa08dce601aaf0f470216fe1b51850b4acf21b179c45070ac7b03a9ac00000000"

    # Bitleu
    if tx_hash_hex == "30cbad942f9fe09d06cabc91773860a827f3625a72eb2ae830c2c8844ffb6de2":
        return "01000000f8141e53010000000000000000000000000000000000000000000000000000000000000000ffffffff1904ffff001d020f27104269746c65752072656c61756e63682effffffff0100000000000000000000000000"

    # Maxcoin
    if tx_hash_hex == "f8cc3b46c273a488c318dc7d98cc053494af2871e495e17f5c7c246055e46af3":  # XXX not sure that's right
        return "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3c04ffff001d01043453686170652d7368696674696e6720736f66747761726520646566656e647320616761696e737420626f746e6574206861636b73ffffffff010065cd1d00000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000"

    # Dash
    if tx_hash_hex == "e0028eb9648db56b1ac77cf090b99048a8007e2bb64b68f092c03c7f56a662c7":
        return "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff6204ffff001d01044c5957697265642030392f4a616e2f3230313420546865204772616e64204578706572696d656e7420476f6573204c6976653a204f76657273746f636b2e636f6d204973204e6f7720416363657074696e6720426974636f696e73ffffffff0100f2052a010000004341040184710fa689ad5023690c80f3a49c8f13f8d45b8c857fbcbc8bc4a8e4d3eb4b10f4d4604fa08dce601aaf0f470216fe1b51850b4acf21b179c45070ac7b03a9ac00000000"

    # BlackCoin
    if tx_hash_hex == "12630d16a97f24b287c8c2594dda5fb98c9e6c70fc61d44191931ea2aa08dc90":
        return "01000000e0df0a53010000000000000000000000000000000000000000000000000000000000000000ffffffff2800012a24323020466562203230313420426974636f696e2041544d7320636f6d6520746f20555341ffffffff0100000000000000000000000000"

    # Unbreakablecoin
    if tx_hash_hex == "e417a7bd4b5d0c0f27caba6bc16963c9dac23a970702336620cc71196f193dfb":
        return "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4e05b1073383000104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff010100000000000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000"
    
    if tx_hash_hex == "d508b7916ec00595c1f8e1c767dc3b37392a5e68adf98118bca80a2ed58331d6":
        return "010000000000000000000000000000000000000000000000000000000000000000ffffffff3804ffff001d010430426172756b204b68617a61642e202042544320426c6f636b20333236313733206e6f6e63653a20383738303136363536"
    
    # Extract your chain's genesis transaction data from the first
    # block file and add it here, or better yet, patch your coin's
    # getrawtransaction to return it on request:
    #if tx_hash_hex == "<HASH>"
    #    return "<DATA>"

    return None
