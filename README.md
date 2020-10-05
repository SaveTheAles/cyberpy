# cyberpy

> Version 0.0.6

> Tools for Cyber wallet management and offline transaction signing

## Installing

#### Installing from PyPI [repository](https://pypi.org/project/cyberpy):

```bash
pip install cyberpy
```

#### Installing from source code:

```bash
git clone https://github.com/SaveTheAles/cyberpy
cd cyberpy
pip3 install .
```

## Usage

### Generating a wallet

```python
from cyberpy import generate_wallet
wallet = generate_wallet()
```

The value assigned to `wallet` will be a dictionary just like:

```python
{
    "seed": "arch skill acquire abuse frown reject front second album pizza hill slogan guess random wonder benefit industry custom green ill moral daring glow elevator",
    "derivation_path": "m/44'/118'/0'/0/0",
    "private_key": b'\xbb\xec^\xf6\xdcg\xe6\xb5\x89\xed\x8cG\x05\x03\xdf0:\xc9\x8b \x85\x8a\x14\x12\xd7\xa6a\x01\xcd\xf8\x88\x93',
    "public_key": b"\x03h\x1d\xae\xa7\x9eO\x8e\xc5\xff\xa3sAw\xe6\xdd\xc9\xb8b\x06\x0eo\xc5a%z\xe3\xff\x1e\xd2\x8e5\xe7",
    "address": "cyber1uuhna3psjqfxnw4msrfzsr0g08yuyfxesqggqd",
}
 ```

### Converter functions

#### Mnemonic seed to private key

```python
from cyberpy import seed_to_privkey
seed = "teach there dream chase fatigue abandon lava super senior artefact close upgrade"
privkey = seed_to_privkey(seed, path="m/44'/118'/0'/0/0")
 ```

#### Private key to public key

```python
from cyberpy import privkey_to_pubkey
privkey = bytes.fromhex("6dcd05d7ac71e09d3cf7da666709ebd59362486ff9e99db0e8bc663570515afa")
pubkey = privkey_to_pubkey(privkey)
 ```

#### Public key to address

```python
from cyberpy import pubkey_to_address
pubkey = bytes.fromhex("03e8005aad74da5a053602f86e3151d4f3214937863a11299c960c28d3609c4775")
addr = pubkey_to_address(pubkey)
 ```

#### Private key to address

```python
from cyberpy import privkey_to_address
privkey = bytes.fromhex("6dcd05d7ac71e09d3cf7da666709ebd59362486ff9e99db0e8bc663570515afa")
addr = privkey_to_address(privkey)
 ```

### Signing transactions

#### Send transaction

```python
from cyberpy import Transaction
tx = Transaction(
    privkey=bytes.fromhex("26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59"),
    account_num=11335,
    sequence=0,
    fee=0,
    gas=200000,
    memo="",
    chain_id="euler-6",
    sync_mode="sync",
)
tx.add_transfer(recipient="cyber103l758ps7403sd9c0y8j6hrfw4xyl70j4mmwkf", amount=387000)
tx.add_transfer(recipient="cyber1lzumfk6xvwf9k9rk72mqtztv867xyem393um48", amount=123)
pushable_tx = tx.get_pushable()
```

One or more token transfers can be added to a transaction by calling the `add_transfer` method.

#### Link transaction

```python
from cyberpy import Transaction
tx = Transaction(
    privkey=bytes.fromhex("26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59"),
    account_num=11335,
    sequence=0,
    fee=0,
    gas=200000,
    memo="",
    chain_id="euler-6",
    sync_mode="sync",
)
tx.add_cyberlink(cid_from="QmceNpj6HfS81PcCaQXrFMQf7LR5FTLkdG9sbSRNy3UXoZ", cid_to="QmRX8qYgeZoYM3M5zzQaWEpVFdpin6FvVXvp6RPQK3oufV")
tx.add_cyberlink(cid_from="QmXsJKAog3tTNEGfHNmSYjdiLYFkq4URrxDpMQpwfBRUtP", cid_to="QmTiXybNXEYbfVEy6bhBSw67u6NHXsB2h36xhwPcCQyRgp")
pushable_tx = tx.get_pushable()
```

One or more cyberlink messages can be added to a transaction by calling the `add_transfer` method.

When the transaction is fully prepared, calling `get_pushable` will return a signed transaction in the form of a JSON string. This can be used as request body when calling the `POST /txs` endpoint of the [cyber REST API](https://lcd.cyber.cybernode.ai/swagger-ui/#/Transactions/post_txs):

```python
import requests

res = requests.post(url=LCD_API+'/txs', data=pushable_tx)
```

All necessary data for tx filling like `account_number` and `sequence` you can get from [cyber REST API](https://api.cyber.cybernode.ai/):

```
https://api.cyber.cybernode.ai/account?address="cyber1uwfk6h06w8vnhmyp48vwcpgwncsec8yv46uan4"
```
