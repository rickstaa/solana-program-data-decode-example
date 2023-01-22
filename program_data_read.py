"""Small example program to read data from a solana smart contract.
"""

import base64
import sys

from solana.rpc.api import Client, Pubkey
from anchorpy import AccountsCoder

PROGRAM_ID = "7sDX4xdZmckRzXMuFAiEVwimH6zph43edCBiHkVa4DeV"  # Escrow-less staking program. # noqa: E501
# PROGRAM_ID = "cndy3Z4yapfJBmL3ShUp5exZKqR3z33thTzeNMm2gRZ"  # Metaplex NFT program.


def main():
    """Main function."""
    if len(sys.argv) != 2:
        print(
            "Usage: python program_data_read.py <program_id>. Example program used "
            f"instead: {PROGRAM_ID}"
        )
        program_id = PROGRAM_ID  # Use example program if no program id is provided
    else:
        program_id = sys.argv[1]

    print("Program id:", program_id)
    client = Client("https://api.mainnet-beta.solana.com")
    account_info = client.get_account_info(
        Pubkey.from_string(program_id), encoding="base58"
    )

    print("Account data:", base64.b64decode(account_info.value.data))
    # print("Account data decoded: ", AccountsCoder.decode(account_info.value.data))


if __name__ == "__main__":
    main()
