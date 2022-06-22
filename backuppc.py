from .agent_based_api.v1 import *

def discover_backuppc(section):
    for pc, lastBackup, lastFullBackup, lastFullSize in section:
        yield Service(item=pc)

def check_backuppc(item, section):
    for pc, ageBackup, ageFullBackup, sizeFullBackup in section:
        if pc == item:
            ageBackup = int(ageBackup)
            ageFullBackup = int(ageFullBackup)
            sizeFullBackup = int(sizeFullBackup)

            yield Metric('ageBackup', ageBackup)
            yield Metric('ageFullBackup', ageFullBackup)
            yield Metric('sizeFullBackup', sizeFullBackup)
            yield Result(
                state=State.OK,
                summary="Last successful backup {:.1f} hours ago".format(ageBackup / 3600.0)
            )
            return

register.check_plugin(
    name = "backuppc",
    service_name = "BackupPC %s",
    discovery_function = discover_backuppc,
    check_function = check_backuppc,
)
