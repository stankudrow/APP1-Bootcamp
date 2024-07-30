class Key:

    def __init__(self) -> None:
        self._passphrase = "zax2rulez"

    def __getitem__(self, key: int):
        return len(str(abs(key)))

    def __gt__(self, other: int) -> bool:
        return other > 9000

    def __len__(self) -> int:
        return 1337

    def __str__(self) -> str:
        return "GeneralTsoKeycard"

    @property
    def passphrase(self) -> str:
        return self._passphrase
