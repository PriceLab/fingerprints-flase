import app.settings
import subprocess
import logging
import tempfile
import json
import os
logger = logging.getLogger('app.api.endpoint.dockerinterface')

class FingerPrintManager(object):
    def __init__(self):
        self.path = app.settings.FINGERPRINT_PATH

    def encode_json(self, json_obj, fp_id, L, normalize=False):
        json_file = self._write_temp_json(json_obj)

        logger.debug("Output json file")
        cmd = ['cat', json_file.name]
        output,error = subprocess.Popen(cmd ,stdout = subprocess.PIPE,
                                        stderr= subprocess.PIPE).communicate()
        logger.debug(output)
        logger.warning(error)

        logger.debug("Running command")
        exe = os.path.join(self.path, 'LPH_JSON.pl')
        cmd = ['perl', exe, json_file.name, fp_id, L]
        if normalize:
            cmd.append('normalize')
        logger.debug(' '.join(cmd))
        output,error = subprocess.Popen(cmd ,stdout = subprocess.PIPE,
                                        stderr= subprocess.PIPE).communicate()
        logger.debug(output)
        logger.warning(error)
        os.unlink(json_file.name)
        res = output.decode('utf-8').strip()
        res = [x.split('\t') for x in res.split('\n')]
        new_res = []
        for r in res:
            new_res.append({'fingerprint_id': r[0],
             'num_triples': r[1],
             'fingerprint': [float(x) for x in  r[2:]],
             'L': len(r) - 2
             })
        return new_res

    def _write_temp_json(self, json_obj):
        f = tempfile.NamedTemporaryFile(mode='w', delete=False)
        json.dump(json_obj, f)
        f.close()
        return f



