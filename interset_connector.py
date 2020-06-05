"""
Copyright 2019 Interset Software Inc.
"""
# Phantom imports
import phantom.app as phantom
from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

import requests
import json

# CONFIGURATION
# query to get/put from importance. Format with TID, entityType, entityId. ex. '/api/tuning/{tid}/importance?entityType={entityType}&entityId={entityId}'
QUERY_IMPORTANCE = '/api/tuning/{}/importance?entityType={}&entityId={}'
# query to get information about given session
API_INFO_SESSION_QUERY = '/api/info/session'
# query to get top risky users for a given tid and user type. Format with TID and userType ex. '/api/search/{tid}/{userType}/topRisky'
QUERY_RISKY_USERS = '/api/search/{}/{}/topRisky'

# CONNECTIVITY TEST STATUS MESSAGES
CONNECTION_SUCCESS_MESSAGE = "Connection successful."
CONFIG_INIT_ERROR_MESSAGE = "Connection failure, make sure persistentSessions is set to 'True' and that the user role is 'admin.\
                            Also ensure the entityId and tid you enter match the values of the authorization token you entered."
AUTH_ERROR_MESSAGE = "Connection failed due to incorrect authorization. Ensure authorization token is correct."
URI_ERROR_MESSAGE = "Connection failed. URI not found."
SERVER_ERROR_MESSAGE = "Connection failure, cannot connect to server."

# ACTION RESULT MESSAGES
IMPORTANCE_SUCCESS = " Execution successful."
IMPORTANCE_AUTH_ERROR = " Execution failed due to incorrect authorization. Ensure tid, entityId and authorization token are correct."
IMPORTANCE_RAND_ERROR = " Execution failed."
SUCCESS_STATUS = "Execution successful."
AUTH_ERROR_STATUS = "Execution failed due to incorrect authorization. Ensure configuration values tid, entityId and authorization token are correct."
RAND_ERROR_STATUS = "Execution failed."
ENTITY_ID_NOT_EXIST_ERROR = "EntityId and EntityType pair do not exist for the configured workflow user"
ENTITY_TYPE_NOT_EXIST_ERROR = "Entity Type does not exist."
MSG_APP_ERROR = 'Msg: APP_ERROR'
MSG_APP_SUCCESS = 'Msg: APP_SUCCESS'

# ACTIONS
TEST_CONNECTIVITY = 'test connectivity'

GET_IMPORTANCE = 'get importance'
PUT_IMPORTANCE = 'put importance'

GET_RISK = 'get risk'
GET_USER_RISK = 'get user risk'
GET_PROJECT_RISK = 'get project risk'
GET_FILE_RISK = 'get file risk'
GET_MACHINE_RISK = 'get device risk'
GET_SERVER_RISK = 'get server risk'

GET_USER_IMPORTANCE = 'get user importance'
GET_PROJECT_IMPORTANCE = 'get project importance'
GET_FILE_IMPORTANCE = 'get file importance'
GET_DEVICE_IMPORTANCE = 'get device importance'

PUT_USER_IMPORTANCE = 'put user importance'
PUT_PROJECT_IMPORTANCE = 'put project importance'
PUT_FILE_IMPORTANCE = 'put file importance'
PUT_DEVICE_IMPORTANCE = 'put device importance'

# Entity Types
USERS = 'users'
PROJECTS = 'projects'
FILES = 'files'
MACHINES = 'machines'
SERVERS = 'servers'
VOLUMES = 'volumes'
PRINTERS = 'printers'
SHARES = 'shares'
RESOURCES = 'resources'
WEBSITES = 'websites'
IPS = 'ips'
DEVICES = 'devices'
VALUE = 'value'
USER = 'user'

# PARAMETER STRINGS
# To access parameter values passed to phantom actions or at configuration, ex. self.params['entityType'] or self.get_config().get(SERVER_URL_CONF)
SERVER_URL_CONF = 'server_url'
ENTITY_TYPE_CONF = 'entityType'
ENTITY_ID_CONF = 'entityId'
AUTH_TOKEN = 'auth_token'

# REQUEST HEADER PARAMETERS
APPLICATION_JSON = 'application/json'
BEARER = 'Bearer '


class IntersetConnector(BaseConnector):

    def __init__(self):

        super(IntersetConnector, self).__init__()

    def initialize(self):

        """
        Called after the config dictionary is validated.
        Initializes necessary variables header, parameter dictionary, and request urls.
        """

        self.debug_print('Initialize')
        self.request_init()
        self.get_importance_url = self.get_config().get(SERVER_URL_CONF) + QUERY_IMPORTANCE.format(self.params['tid'], self.params[ENTITY_TYPE_CONF], self.params[ENTITY_ID_CONF])
        self.test_conn_url = self.get_config().get(SERVER_URL_CONF) + API_INFO_SESSION_QUERY
        self.entity_list_url = self.get_config().get(SERVER_URL_CONF) + QUERY_RISKY_USERS

        return phantom.APP_SUCCESS

    def finalize(self):
        self.debug_print('Finalize')
        return

    def handle_exception(self, exception_object):
        self.debug_print('Handle Exception')

    def get_user_importance(self, param):
        param[ENTITY_TYPE_CONF] = USERS[:-1]
        self.get_importance(param)

    def get_file_importance(self, param):
        param[ENTITY_TYPE_CONF] = FILES[:-1]
        self.get_importance(param)

    def get_device_importance(self, param):
        param[ENTITY_TYPE_CONF] = MACHINES[:-1]
        self.get_importance(param)

    def get_project_importance(self, param):
        param[ENTITY_TYPE_CONF] = PROJECTS[:-1]
        self.get_importance(param)

    def put_user_importance(self, param):
        param[ENTITY_TYPE_CONF] = USERS[:-1]
        self.put_importance(param)

    def put_file_importance(self, param):
        param[ENTITY_TYPE_CONF] = FILES[:-1]
        self.put_importance(param)

    def put_device_importance(self, param):
        param[ENTITY_TYPE_CONF] = MACHINES[:-1]
        self.put_importance(param)

    def put_project_importance(self, param):
        param[ENTITY_TYPE_CONF] = PROJECTS[:-1]
        self.put_importance(param)

    def get_user_risk(self, param):
        param[ENTITY_TYPE_CONF] = USERS[:-1]
        self.get_risk(param)

    def get_file_risk(self, param):
        param[ENTITY_TYPE_CONF] = FILES[:-1]
        self.get_risk(param)

    def get_device_risk(self, param):
        param[ENTITY_TYPE_CONF] = MACHINES[:-1]
        self.get_risk(param)

    def get_project_risk(self, param):
        param[ENTITY_TYPE_CONF] = PROJECTS[:-1]
        self.get_risk(param)

    def request_init(self):

        """
        Initializes header and parameter dictionaries for actions.
        """

        self.HEADER = {
            'Content-Type': APPLICATION_JSON,
            'Accept': APPLICATION_JSON,
            'Authorization': BEARER + self.get_config().get(AUTH_TOKEN)
        }

        self.params = {
            'tid': self.get_config().get('tid'),
            'entityId': self.get_config().get(ENTITY_ID_CONF),
            'entityType': USER
        }

        # parameters to query list of entitys
        self.risky_params = {
            'sort': 'current',
            'q': '',
            'markup': 'false',
            'tz': 'UTC',
            'count': '10',
            'keepAlive': '300000'
        }

        # successful response codes.
        self.successful_response_codes = set()
        self.successful_response_codes.add(requests.codes.ok)
        self.successful_response_codes.add(requests.codes.no_content)

        self.entity_types = set()
        self.entity_types.add(USERS)
        self.entity_types.add(PROJECTS)
        self.entity_types.add(FILES)
        self.entity_types.add(MACHINES)
        self.entity_types.add(VOLUMES)
        self.entity_types.add(PRINTERS)
        self.entity_types.add(SHARES)
        self.entity_types.add(RESOURCES)
        self.entity_types.add(WEBSITES)
        self.entity_types.add(IPS)
        self.entity_types.add(DEVICES)

    def set_entity_type(self, param):
        entityType = str(param[ENTITY_TYPE_CONF]) + 's'
        if entityType == DEVICES:
            param[ENTITY_TYPE_CONF] = MACHINES[:-1]
            return MACHINES
        return entityType

    def set_response_status(self, response, action_result):
        """
        Sets status of a action result depending on the response of a given request.
        """
        if not response:
            self.set_status_save_progress(phantom.APP_ERROR, MSG_APP_ERROR)
        else:
            self.set_status_save_progress(phantom.APP_SUCCESS, MSG_APP_SUCCESS)
            action_result.set_status(phantom.APP_SUCCESS)

    def handle_response(self, response, action_result):

        """
        Method to check if a response was successful and set the appropriate action result based on the status code of the response.

        Returns a boolean value to indicate if the response was successful
        """

        if response.status_code in self.successful_response_codes:
            action_result.set_status(phantom.APP_SUCCESS, SUCCESS_STATUS, None)
            return True
        elif response.status_code == requests.codes.unauthorized:
            action_result.set_status(phantom.APP_ERROR, AUTH_ERROR_STATUS, None)
        else:
            action_result.set_status(phantom.APP_ERROR, RAND_ERROR_STATUS, None)
        return False

    def entity_exists(self, entityId, entityType, action_result):

        """
        Method to check if a entityId and entityType pair exists for the configured workflow user. In the case the pair does not exist,
        a action result is set with the appropriate error.

        Returns a boolean value to indicate if the pair exists.
        """

        q_entity_type = entityType[:-1] + ':'
        self.risky_params['q'] = q_entity_type + entityId

        try:
            top_risky_response = requests.get(self.entity_list_url.format(self.params['tid'], entityType), headers=self.HEADER, params=self.risky_params, verify=False)
        except requests.ConnectionError as e:
            action_result.set_status(phantom.APP_ERROR, SERVER_ERROR_MESSAGE, e)
            self.set_status_save_progress(phantom.APP_ERROR, SERVER_ERROR_MESSAGE)
            return

        if self.handle_response(top_risky_response, action_result):
            if len(top_risky_response.json()['data']) < 1:
                action_result.set_status(phantom.APP_ERROR, ENTITY_ID_NOT_EXIST_ERROR, None)
                return False
            return True

        return False

    def entity_valid(self, param, action_result):

        """
        Method to check if the entityType and entityId are valid. Checks if entity type is in the set of possible types. Then
        executes the entity_exists method to check if the entityId and entityType pair exists for the configured workflow user.
        """

        entityType = param[ENTITY_TYPE_CONF]
        entityId = param[ENTITY_ID_CONF]

        if entityType + 's' not in self.entity_types:
            action_result.set_status(phantom.APP_ERROR, ENTITY_TYPE_NOT_EXIST_ERROR, None)
            return False

        if not self.entity_exists(param[ENTITY_ID_CONF], entityType + 's', action_result):
            return False

        self.params[ENTITY_TYPE_CONF] = entityType
        self.params[ENTITY_ID_CONF] = entityId

        return True

    def _test_connectivity(self, param):

        """
        Executed when the user presses 'test connectivity' in the phantom UI. Used to check the validity of the
        configuration when creating an asset.
        Makes a get request to 'http://application.ad.interset.com/api/info/session' to get information about
        a given user.
        Ensures the server can be reached, that the auth token is correct, and that the user is a 'admin' and persistentSessions are set to true.
        """

        try:
            response = requests.get(self.test_conn_url, headers=self.HEADER, verify=False)
        except requests.ConnectionError:
            message = SERVER_ERROR_MESSAGE
            return self.set_status_save_progress(phantom.APP_ERROR, message)

        if response.status_code == requests.codes.ok:
            if response.json()['persistentSessions'] is True and response.json()['roles'][0]['role'] == 'admin' and \
                    response.json()['userId'] == self.params[ENTITY_ID_CONF] and response.json()['roles'][0]['tenantId'] == self.params['tid']:
                message = CONNECTION_SUCCESS_MESSAGE
                return self.set_status_save_progress(phantom.APP_SUCCESS, message)
            else:
                message = CONFIG_INIT_ERROR_MESSAGE
                return self.set_status_save_progress(phantom.APP_ERROR, message)
        elif response.status_code == requests.codes.unauthorized:
            message = AUTH_ERROR_MESSAGE
            return self.set_status_save_progress(phantom.APP_ERROR, message)
        else:
            message = URI_ERROR_MESSAGE
            return self.set_status_save_progress(phantom.APP_ERROR, message)

    def get_importance(self, param):

        """
        Executed by a phantom.act() call on the 'get importance' action or called by the get_'entity'_importance actions.
        Gets importance of the user that was used to configure the asset.
        """

        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        self.set_entity_type(param)

        if not self.entity_valid(param, action_result):
            return

        self.get_importance_url = self.get_config().get(SERVER_URL_CONF) + QUERY_IMPORTANCE.format(self.params['tid'], self.params[ENTITY_TYPE_CONF], self.params[ENTITY_ID_CONF])

        try:
            response = requests.get(self.get_importance_url, headers=self.HEADER, verify=False)
        except requests.ConnectionError as e:
            action_result.set_status(phantom.APP_ERROR, SERVER_ERROR_MESSAGE, e)
            self.set_status_save_progress(phantom.APP_ERROR, SERVER_ERROR_MESSAGE)
            return

        if self.handle_response(response, action_result):
            action_result.add_data(json.loads(response.text))
            return action_result.get_status()

    def put_importance(self, param):

        """
        Executed by a phantom.act() call on the 'put importance' action or called by the put_'entity'_importance actions.
        Sets the importance of the user that was used to configure the asset to the numerical value passed as a parameter.
        """
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        self.set_entity_type(param)

        if not self.entity_valid(param, action_result):
            return

        body = {'value': param[VALUE]}

        self.get_importance_url = self.get_config().get(SERVER_URL_CONF) + QUERY_IMPORTANCE.format(self.params['tid'], self.params[ENTITY_TYPE_CONF], self.params[ENTITY_ID_CONF])

        try:
            response = requests.put(self.get_importance_url, data=json.dumps(body), headers=self.HEADER, verify=False)
        except requests.ConnectionError as e:
            action_result.set_status(phantom.APP_ERROR, SERVER_ERROR_MESSAGE, e)
            return

        if self.handle_response(response, action_result):
            return action_result.get_status()

    def get_risk(self, param):

        """
        Executed by the phatnom.act() call on the 'get risk' action or by the get_'something'_risk actions.
        Passed the param value that was passed through a phantom.act(..) call, and the entityType of the corresponding action.

        Checks if the entityId passed in 'param' exists for the given entityType. If the entityId exists, the api
        is queried and the risk score value is added to the action_result's data field.
        Otherwise an appropriate error message is generated.
        """

        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        entityType = self.set_entity_type(param)

        if not self.entity_valid(param, action_result):
            return

        q_entity_type = entityType[:-1] + ':'
        self.risky_params['q'] = q_entity_type + str(param[ENTITY_ID_CONF])

        try:
            response = requests.get(self.entity_list_url.format(self.params['tid'], entityType), headers=self.HEADER, params=self.risky_params, verify=False)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, SERVER_ERROR_MESSAGE, e)
            return

        if self.handle_response(response, action_result):
            action_result.add_data(json.loads(response.text))
            return action_result.get_status()

    def handle_action(self, param):

        """
        Implements functionality for the appConnector. It is called for every paramater dictionary element in
        the paramaters array. It then gets the action identifier and calls the member function that handles this action.
        """

        # Gets action identifier
        action_id = self.get_action_identifier()

        actions = {
            TEST_CONNECTIVITY: self._test_connectivity,
            GET_IMPORTANCE: self.get_importance,
            PUT_IMPORTANCE: self.put_importance,
            GET_RISK: self.get_risk,
            GET_USER_RISK: self.get_user_risk,
            GET_FILE_RISK: self.get_file_risk,
            GET_MACHINE_RISK: self.get_device_risk,
            GET_PROJECT_RISK: self.get_project_risk,
            GET_USER_IMPORTANCE: self.get_user_importance,
            GET_PROJECT_IMPORTANCE: self.get_project_importance,
            GET_FILE_IMPORTANCE: self.get_file_importance,
            GET_DEVICE_IMPORTANCE: self.get_device_importance,
            PUT_USER_IMPORTANCE: self.put_user_importance,
            PUT_PROJECT_IMPORTANCE: self.put_project_importance,
            PUT_FILE_IMPORTANCE: self.put_file_importance,
            PUT_DEVICE_IMPORTANCE: self.put_device_importance

        }

        run_action = actions[action_id]
        return run_action(param)


if __name__ == '__main__':

    import sys

    if (len(sys.argv) < 2):
        print 'No test json specified as input'
        exit(0)

    with open(sys.argv[1]) as f:                           # input a json file that contains data like the configuration and action parameters,
        in_json = f.read()
        in_json = json.loads(in_json)
        print ('%s %s' % (sys.argv[1], json.dumps(in_json, indent=4)))

        connector = IntersetConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    exit(0)
