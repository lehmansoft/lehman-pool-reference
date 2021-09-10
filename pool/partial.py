from dataclasses import dataclass

from blspy import G1Element
from chia.pools.pool_wallet_info import PoolState
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.types.coin_spend import CoinSpend
from chia.util.ints import uint64
from chia.util.streamable import streamable, Streamable


@dataclass(frozen=True)
@streamable
class PartialRecord(Streamable):
    launcher_id: bytes32 
    timestamp: uint64  
    difficulty: uint64  
    challenge: str  
    pool_contract_puzzle_hash: str
    plot_public_key: str
    size: uint64
    proof: str
    sp_hash: str
    end_of_sub_slot: bool  
    harvester_id: str 
    valid:bool
    invalid_error:str 

    def setValid(self,valid,error):
        self.valid=valid
        self.invalid_error=error