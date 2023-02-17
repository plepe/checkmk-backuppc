## INSTALL
On the monitoring client:
```sh
REPO=/path/to/repo
ln -s $REPO/backuppc /usr/lib/check_mk_agent/plugins/backuppc
```

On the monitoring server:
```sh
REPO=/path/to/repo
SITE=cvast
ln -s $REPO/backuppc_metric.py /opt/omd/sites/$SITE/local/share/check_mk/web/plugins/metrics/backuppc_metric.py
ln -s $REPO/backuppc_metric.py /opt/omd/sites/$SITE/local/share/check_mk/web/plugins/wato/backuppc_parameters.py
ln -s $REPO/backuppc.py /opt/omd/sites/$SITE/local/lib/python3/cmk/base/plugins/agent_based/backuppc.py
```
