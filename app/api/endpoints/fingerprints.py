import logging
import subprocess

from flask import request
from flask_restplus import Resource
from app.api.restplus import api
from app.business.fingerprintsapi import FingerPrintManager
from app.api.parsers.fingerprints_serial import *

logger = logging.getLogger('app.api.endpoints.fingerprints')

ns = api.namespace('fingerprints', 
        description="""Data Fingerprint endpoints""")

@ns.route('/encode')
class Encode(Resource):
    @ns.doc(model=encode_response)
    @ns.expect(encode_request)#, validate=False)
    def post(self):
        """Encode a list of json objects to fingerprints"""
        req = request.json
        response = {}
        response_code = 200
        try:
            fpm = FingerPrintManager()
            results = fpm.encode_json(req['items'], req['fingerprint_id'], 
                    "%i" % req['L'], normalize=req['normalize'])
            response['data'] = results
        except Exception as e:
            response['error'] = {'type':str(type(e)), 'code':500,'message':str(e)}
            response_code = 500
            logger.exception("Error creating fingerprint")
        return response, response_code

