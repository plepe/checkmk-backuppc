from .agent_based_api.v1 import *

def discover_backuppc(section):
    for pc, lastBackup, lastFullBackup, lastFullSize in section:
        yield Service(item=pc)

def check_backuppc(item, params, section):
    for pc, ageBackup, ageFullBackup, sizeFullBackup in section:
        if pc == item:
            ageBackup = int(ageBackup)
            ageFullBackup = int(ageFullBackup)
            sizeFullBackup = int(sizeFullBackup)
            state = State.OK
            if ageBackup / 3600 > params["critical_age"]:
                state = State.CRIT
            elif ageBackup / 3600 > params["warning_age"]:
                state = State.WARN

            yield Metric('ageBackup', ageBackup)
            yield Metric('ageFullBackup', ageFullBackup)
            yield Metric('sizeFullBackup', sizeFullBackup)
            yield Result(
                state=state,
                summary="Last successful backup {:.1f} hours ago".format(ageBackup / 3600.0)
            )
            return

register.check_plugin(
    name = "backuppc",
    service_name = "BackupPC %s",
    discovery_function = discover_backuppc,
    check_default_parameters = {"warning_age": 24, "critical_age": 48},
    check_ruleset_name = "backuppc",
    check_function = check_backuppc,
)
