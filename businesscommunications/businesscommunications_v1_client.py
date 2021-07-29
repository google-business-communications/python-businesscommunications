"""Generated client library for businesscommunications version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from . import businesscommunications_v1_messages as messages


class BusinesscommunicationsV1(base_api.BaseApiClient):
  """Generated client library for service businesscommunications version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://businesscommunications.googleapis.com/'
  MTLS_BASE_URL = 'https://businesscommunications.mtls.googleapis.com/'

  _PACKAGE = 'businesscommunications'
  _SCOPES = ['https://www.googleapis.com/auth/userinfo.email']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = 'BusinesscommunicationsV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new businesscommunications handle."""
    url = url or self.BASE_URL
    super(BusinesscommunicationsV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.brands_agents = self.BrandsAgentsService(self)
    self.brands_locations = self.BrandsLocationsService(self)
    self.brands = self.BrandsService(self)
    self.partners = self.PartnersService(self)

  class BrandsAgentsService(base_api.BaseApiService):
    """Service class for the brands_agents resource."""

    _NAME = 'brands_agents'

    def __init__(self, client):
      super(BusinesscommunicationsV1.BrandsAgentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new agent to represent a brand.

      Args:
        request: (BusinesscommunicationsBrandsAgentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Agent) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/agents',
        http_method='POST',
        method_id='businesscommunications.brands.agents.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/agents',
        request_field='agent',
        request_type_name='BusinesscommunicationsBrandsAgentsCreateRequest',
        response_type_name='Agent',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes an agent. The delete request fails if any `brands.agents.requestVerification` requests have been made for the agent.

      Args:
        request: (BusinesscommunicationsBrandsAgentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/agents/{agentsId}',
        http_method='DELETE',
        method_id='businesscommunications.brands.agents.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsAgentsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get information about an agent.

      Args:
        request: (BusinesscommunicationsBrandsAgentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Agent) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/agents/{agentsId}',
        http_method='GET',
        method_id='businesscommunications.brands.agents.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsAgentsGetRequest',
        response_type_name='Agent',
        supports_download=False,
    )

    def GetLaunch(self, request, global_params=None):
      r"""Gets the launch information for an agent.

      Args:
        request: (BusinesscommunicationsBrandsAgentsGetLaunchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AgentLaunch) The response message.
      """
      config = self.GetMethodConfig('GetLaunch')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetLaunch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/agents/{agentsId}/launch',
        http_method='GET',
        method_id='businesscommunications.brands.agents.getLaunch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsAgentsGetLaunchRequest',
        response_type_name='AgentLaunch',
        supports_download=False,
    )

    def GetVerification(self, request, global_params=None):
      r"""Gets the verification information for an agent.

      Args:
        request: (BusinesscommunicationsBrandsAgentsGetVerificationRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AgentVerification) The response message.
      """
      config = self.GetMethodConfig('GetVerification')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetVerification.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/agents/{agentsId}/verification',
        http_method='GET',
        method_id='businesscommunications.brands.agents.getVerification',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsAgentsGetVerificationRequest',
        response_type_name='AgentVerification',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all the agents associated with a brand. *Note*: This method always sets `pageSize` to `0`.

      Args:
        request: (BusinesscommunicationsBrandsAgentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAgentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/agents',
        http_method='GET',
        method_id='businesscommunications.brands.agents.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/agents',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsAgentsListRequest',
        response_type_name='ListAgentsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates information about an agent. *Caution*: If you update a field that takes a list as input, you must include the entire list in the update request. Updates to list fields replace the entire list.

      Args:
        request: (BusinesscommunicationsBrandsAgentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Agent) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/agents/{agentsId}',
        http_method='PATCH',
        method_id='businesscommunications.brands.agents.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='agent',
        request_type_name='BusinesscommunicationsBrandsAgentsPatchRequest',
        response_type_name='Agent',
        supports_download=False,
    )

    def RequestLaunch(self, request, global_params=None):
      r"""Begins the launch process for an agent. An agent is available to users after it launches. An agent can only have one instance of launch at a time.

      Args:
        request: (BusinesscommunicationsBrandsAgentsRequestLaunchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AgentLaunch) The response message.
      """
      config = self.GetMethodConfig('RequestLaunch')
      return self._RunMethod(
          config, request, global_params=global_params)

    RequestLaunch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/agents/{agentsId}:requestLaunch',
        http_method='POST',
        method_id='businesscommunications.brands.agents.requestLaunch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:requestLaunch',
        request_field='requestAgentLaunchRequest',
        request_type_name='BusinesscommunicationsBrandsAgentsRequestLaunchRequest',
        response_type_name='AgentLaunch',
        supports_download=False,
    )

    def RequestVerification(self, request, global_params=None):
      r"""Begins business information verification for an agent. Google contacts the brand for verification. Only 1 instance of verification is allowed at any given time.

      Args:
        request: (BusinesscommunicationsBrandsAgentsRequestVerificationRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AgentVerification) The response message.
      """
      config = self.GetMethodConfig('RequestVerification')
      return self._RunMethod(
          config, request, global_params=global_params)

    RequestVerification.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/agents/{agentsId}:requestVerification',
        http_method='POST',
        method_id='businesscommunications.brands.agents.requestVerification',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:requestVerification',
        request_field='requestAgentVerificationRequest',
        request_type_name='BusinesscommunicationsBrandsAgentsRequestVerificationRequest',
        response_type_name='AgentVerification',
        supports_download=False,
    )

    def UpdateLaunch(self, request, global_params=None):
      r"""Updates the launch information for an agent.

      Args:
        request: (BusinesscommunicationsBrandsAgentsUpdateLaunchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AgentLaunch) The response message.
      """
      config = self.GetMethodConfig('UpdateLaunch')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateLaunch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/agents/{agentsId}/launch',
        http_method='PATCH',
        method_id='businesscommunications.brands.agents.updateLaunch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='agentLaunch',
        request_type_name='BusinesscommunicationsBrandsAgentsUpdateLaunchRequest',
        response_type_name='AgentLaunch',
        supports_download=False,
    )

    def UpdateVerification(self, request, global_params=None):
      r"""Updates the verification state for an agent.

      Args:
        request: (BusinesscommunicationsBrandsAgentsUpdateVerificationRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AgentVerification) The response message.
      """
      config = self.GetMethodConfig('UpdateVerification')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateVerification.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/agents/{agentsId}/verification',
        http_method='PATCH',
        method_id='businesscommunications.brands.agents.updateVerification',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='agentVerification',
        request_type_name='BusinesscommunicationsBrandsAgentsUpdateVerificationRequest',
        response_type_name='AgentVerification',
        supports_download=False,
    )

  class BrandsLocationsService(base_api.BaseApiService):
    """Service class for the brands_locations resource."""

    _NAME = 'brands_locations'

    def __init__(self, client):
      super(BusinesscommunicationsV1.BrandsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new location for a brand.

      Args:
        request: (BusinesscommunicationsBrandsLocationsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/locations',
        http_method='POST',
        method_id='businesscommunications.brands.locations.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/locations',
        request_field='location',
        request_type_name='BusinesscommunicationsBrandsLocationsCreateRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a location. The delete request fails if any `brands.locations.requestVerification` requests have been made for the location.

      Args:
        request: (BusinesscommunicationsBrandsLocationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/locations/{locationsId}',
        http_method='DELETE',
        method_id='businesscommunications.brands.locations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsLocationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get information about a location.

      Args:
        request: (BusinesscommunicationsBrandsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/locations/{locationsId}',
        http_method='GET',
        method_id='businesscommunications.brands.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def GetLaunch(self, request, global_params=None):
      r"""Gets the launch information for a location.

      Args:
        request: (BusinesscommunicationsBrandsLocationsGetLaunchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LocationLaunch) The response message.
      """
      config = self.GetMethodConfig('GetLaunch')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetLaunch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/locations/{locationsId}/launch',
        http_method='GET',
        method_id='businesscommunications.brands.locations.getLaunch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsLocationsGetLaunchRequest',
        response_type_name='LocationLaunch',
        supports_download=False,
    )

    def GetVerification(self, request, global_params=None):
      r"""Gets the verification information for a location.

      Args:
        request: (BusinesscommunicationsBrandsLocationsGetVerificationRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LocationVerification) The response message.
      """
      config = self.GetMethodConfig('GetVerification')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetVerification.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/locations/{locationsId}/verification',
        http_method='GET',
        method_id='businesscommunications.brands.locations.getVerification',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsLocationsGetVerificationRequest',
        response_type_name='LocationVerification',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all the locations for a brand. *Note*: This method always sets `pageSize` to `0`.

      Args:
        request: (BusinesscommunicationsBrandsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/locations',
        http_method='GET',
        method_id='businesscommunications.brands.locations.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/locations',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates information about a location. *Caution*: If you update a field that takes a list as input, you must include the entire list in the update request. Updates to list fields replace the entire list.

      Args:
        request: (BusinesscommunicationsBrandsLocationsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/locations/{locationsId}',
        http_method='PATCH',
        method_id='businesscommunications.brands.locations.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='location',
        request_type_name='BusinesscommunicationsBrandsLocationsPatchRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def RequestLaunch(self, request, global_params=None):
      r"""Begins the launch process for a location. A location is available to users after it launches. A location can only have one instance of launch at a time. If the location hasn't been launched previously, sets the launch status to `PENDING`.

      Args:
        request: (BusinesscommunicationsBrandsLocationsRequestLaunchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LocationLaunch) The response message.
      """
      config = self.GetMethodConfig('RequestLaunch')
      return self._RunMethod(
          config, request, global_params=global_params)

    RequestLaunch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/locations/{locationsId}:requestLaunch',
        http_method='POST',
        method_id='businesscommunications.brands.locations.requestLaunch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:requestLaunch',
        request_field='requestLocationLaunchRequest',
        request_type_name='BusinesscommunicationsBrandsLocationsRequestLaunchRequest',
        response_type_name='LocationLaunch',
        supports_download=False,
    )

    def RequestVerification(self, request, global_params=None):
      r"""Begins verification for a location. A location is available for use after it's verified. A location can only have one instance of verification at a time. If the location status hasn't been verified previously, sets the status to `PENDING`.

      Args:
        request: (BusinesscommunicationsBrandsLocationsRequestVerificationRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LocationVerification) The response message.
      """
      config = self.GetMethodConfig('RequestVerification')
      return self._RunMethod(
          config, request, global_params=global_params)

    RequestVerification.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/locations/{locationsId}:requestVerification',
        http_method='POST',
        method_id='businesscommunications.brands.locations.requestVerification',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:requestVerification',
        request_field='requestLocationVerificationRequest',
        request_type_name='BusinesscommunicationsBrandsLocationsRequestVerificationRequest',
        response_type_name='LocationVerification',
        supports_download=False,
    )

    def UpdateLaunch(self, request, global_params=None):
      r"""Updates the launch information for a location.

      Args:
        request: (BusinesscommunicationsBrandsLocationsUpdateLaunchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LocationLaunch) The response message.
      """
      config = self.GetMethodConfig('UpdateLaunch')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateLaunch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}/locations/{locationsId}/launch',
        http_method='PATCH',
        method_id='businesscommunications.brands.locations.updateLaunch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='locationLaunch',
        request_type_name='BusinesscommunicationsBrandsLocationsUpdateLaunchRequest',
        response_type_name='LocationLaunch',
        supports_download=False,
    )

  class BrandsService(base_api.BaseApiService):
    """Service class for the brands resource."""

    _NAME = 'brands'

    def __init__(self, client):
      super(BusinesscommunicationsV1.BrandsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new brand.

      Args:
        request: (Brand) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Brand) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='businesscommunications.brands.create',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1/brands',
        request_field='<request>',
        request_type_name='Brand',
        response_type_name='Brand',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a brand. If the brand has any associated agents or locations, the delete request fails unless `force` is `true`.

      Args:
        request: (BusinesscommunicationsBrandsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}',
        http_method='DELETE',
        method_id='businesscommunications.brands.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['force'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information about a brand.

      Args:
        request: (BusinesscommunicationsBrandsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Brand) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}',
        http_method='GET',
        method_id='businesscommunications.brands.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsGetRequest',
        response_type_name='Brand',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all the brands accessible to the user making the request. *Note*: This method always sets `pageSize` to `0`.

      Args:
        request: (BusinesscommunicationsBrandsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListBrandsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='businesscommunications.brands.list',
        ordered_params=[],
        path_params=[],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/brands',
        request_field='',
        request_type_name='BusinesscommunicationsBrandsListRequest',
        response_type_name='ListBrandsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates information about a brand. *Caution*: If you update a field that takes a list as input, you must include the entire list in the update request. Updates to list fields replace the entire list.

      Args:
        request: (BusinesscommunicationsBrandsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Brand) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/brands/{brandsId}',
        http_method='PATCH',
        method_id='businesscommunications.brands.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='brand',
        request_type_name='BusinesscommunicationsBrandsPatchRequest',
        response_type_name='Brand',
        supports_download=False,
    )

  class PartnersService(base_api.BaseApiService):
    """Service class for the partners resource."""

    _NAME = 'partners'

    def __init__(self, client):
      super(BusinesscommunicationsV1.PartnersService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Get the information about the partner.

      Args:
        request: (BusinesscommunicationsPartnersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Partner) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/partners/{partnersId}',
        http_method='GET',
        method_id='businesscommunications.partners.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='BusinesscommunicationsPartnersGetRequest',
        response_type_name='Partner',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the information for a partner.

      Args:
        request: (BusinesscommunicationsPartnersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Partner) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/partners/{partnersId}',
        http_method='PATCH',
        method_id='businesscommunications.partners.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='partner',
        request_type_name='BusinesscommunicationsPartnersPatchRequest',
        response_type_name='Partner',
        supports_download=False,
    )
