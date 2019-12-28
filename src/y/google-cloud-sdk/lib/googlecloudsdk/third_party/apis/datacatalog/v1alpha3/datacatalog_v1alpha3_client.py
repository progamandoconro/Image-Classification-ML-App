"""Generated client library for datacatalog version v1alpha3."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.datacatalog.v1alpha3 import datacatalog_v1alpha3_messages as messages


class DatacatalogV1alpha3(base_api.BaseApiClient):
  """Generated client library for service datacatalog version v1alpha3."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://datacatalog.googleapis.com/'

  _PACKAGE = u'datacatalog'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1alpha3'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'DatacatalogV1alpha3'
  _URL_VERSION = u'v1alpha3'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new datacatalog handle."""
    url = url or self.BASE_URL
    super(DatacatalogV1alpha3, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_crawlers_crawlerRuns = self.ProjectsCrawlersCrawlerRunsService(self)
    self.projects_crawlers = self.ProjectsCrawlersService(self)
    self.projects_taxonomies_categories = self.ProjectsTaxonomiesCategoriesService(self)
    self.projects_taxonomies = self.ProjectsTaxonomiesService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsCrawlersCrawlerRunsService(base_api.BaseApiService):
    """Service class for the projects_crawlers_crawlerRuns resource."""

    _NAME = u'projects_crawlers_crawlerRuns'

    def __init__(self, client):
      super(DatacatalogV1alpha3.ProjectsCrawlersCrawlerRunsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets a particular run of the crawler.

      Args:
        request: (DatacatalogProjectsCrawlersCrawlerRunsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3CrawlerRun) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/crawlers/{crawlersId}/crawlerRuns/{crawlerRunsId}',
        http_method=u'GET',
        method_id=u'datacatalog.projects.crawlers.crawlerRuns.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha3/{+name}',
        request_field='',
        request_type_name=u'DatacatalogProjectsCrawlersCrawlerRunsGetRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3CrawlerRun',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists crawler runs. This includes the currently running, pending and.
completed crawler runs.

      Args:
        request: (DatacatalogProjectsCrawlersCrawlerRunsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3ListCrawlerRunsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/crawlers/{crawlersId}/crawlerRuns',
        http_method=u'GET',
        method_id=u'datacatalog.projects.crawlers.crawlerRuns.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha3/{+parent}/crawlerRuns',
        request_field='',
        request_type_name=u'DatacatalogProjectsCrawlersCrawlerRunsListRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3ListCrawlerRunsResponse',
        supports_download=False,
    )

  class ProjectsCrawlersService(base_api.BaseApiService):
    """Service class for the projects_crawlers resource."""

    _NAME = u'projects_crawlers'

    def __init__(self, client):
      super(DatacatalogV1alpha3.ProjectsCrawlersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new crawler in a project. The request fails if the crawler.
(`parent`, crawlerId) exists.

      Args:
        request: (DatacatalogProjectsCrawlersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3Crawler) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/crawlers',
        http_method=u'POST',
        method_id=u'datacatalog.projects.crawlers.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'crawlerId'],
        relative_path=u'v1alpha3/{+parent}/crawlers',
        request_field=u'googleCloudDatacatalogV1alpha3Crawler',
        request_type_name=u'DatacatalogProjectsCrawlersCreateRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3Crawler',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a crawler in a project. The request fails if the crawler does.
not exist.

      Args:
        request: (DatacatalogProjectsCrawlersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/crawlers/{crawlersId}',
        http_method=u'DELETE',
        method_id=u'datacatalog.projects.crawlers.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha3/{+name}',
        request_field='',
        request_type_name=u'DatacatalogProjectsCrawlersDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a crawler in a project.

      Args:
        request: (DatacatalogProjectsCrawlersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3Crawler) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/crawlers/{crawlersId}',
        http_method=u'GET',
        method_id=u'datacatalog.projects.crawlers.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha3/{+name}',
        request_field='',
        request_type_name=u'DatacatalogProjectsCrawlersGetRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3Crawler',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the crawlers in a project.

      Args:
        request: (DatacatalogProjectsCrawlersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3ListCrawlersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/crawlers',
        http_method=u'GET',
        method_id=u'datacatalog.projects.crawlers.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha3/{+parent}/crawlers',
        request_field='',
        request_type_name=u'DatacatalogProjectsCrawlersListRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3ListCrawlersResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a crawler in a project.

      Args:
        request: (DatacatalogProjectsCrawlersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3Crawler) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/crawlers/{crawlersId}',
        http_method=u'PATCH',
        method_id=u'datacatalog.projects.crawlers.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha3/{+name}',
        request_field=u'googleCloudDatacatalogV1alpha3Crawler',
        request_type_name=u'DatacatalogProjectsCrawlersPatchRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3Crawler',
        supports_download=False,
    )

    def Run(self, request, global_params=None):
      r"""Runs a crawler will create and execute an ad-hoc crawler run.
The request fails if the crawler is already running.

      Args:
        request: (DatacatalogProjectsCrawlersRunRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3CrawlerRun) The response message.
      """
      config = self.GetMethodConfig('Run')
      return self._RunMethod(
          config, request, global_params=global_params)

    Run.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/crawlers/{crawlersId}:run',
        http_method=u'POST',
        method_id=u'datacatalog.projects.crawlers.run',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha3/{+name}:run',
        request_field=u'googleCloudDatacatalogV1alpha3RunCrawlerRequest',
        request_type_name=u'DatacatalogProjectsCrawlersRunRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3CrawlerRun',
        supports_download=False,
    )

  class ProjectsTaxonomiesCategoriesService(base_api.BaseApiService):
    """Service class for the projects_taxonomies_categories resource."""

    _NAME = u'projects_taxonomies_categories'

    def __init__(self, client):
      super(DatacatalogV1alpha3.ProjectsTaxonomiesCategoriesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a category in a taxonomy.

      Args:
        request: (DatacatalogProjectsTaxonomiesCategoriesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3Category) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}/categories',
        http_method=u'POST',
        method_id=u'datacatalog.projects.taxonomies.categories.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha3/{+parent}/categories',
        request_field=u'googleCloudDatacatalogV1alpha3Category',
        request_type_name=u'DatacatalogProjectsTaxonomiesCategoriesCreateRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3Category',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a category. Also deletes all of its descendant categories.

      Args:
        request: (DatacatalogProjectsTaxonomiesCategoriesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}/categories/{categoriesId}',
        http_method=u'DELETE',
        method_id=u'datacatalog.projects.taxonomies.categories.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha3/{+name}',
        request_field='',
        request_type_name=u'DatacatalogProjectsTaxonomiesCategoriesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a category.

      Args:
        request: (DatacatalogProjectsTaxonomiesCategoriesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3Category) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}/categories/{categoriesId}',
        http_method=u'GET',
        method_id=u'datacatalog.projects.taxonomies.categories.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha3/{+name}',
        request_field='',
        request_type_name=u'DatacatalogProjectsTaxonomiesCategoriesGetRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3Category',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the IAM policy for a taxonomy or a category.

      Args:
        request: (DatacatalogProjectsTaxonomiesCategoriesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}/categories/{categoriesId}:getIamPolicy',
        http_method=u'POST',
        method_id=u'datacatalog.projects.taxonomies.categories.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha3/{+resource}:getIamPolicy',
        request_field=u'getIamPolicyRequest',
        request_type_name=u'DatacatalogProjectsTaxonomiesCategoriesGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all categories in a taxonomy.

      Args:
        request: (DatacatalogProjectsTaxonomiesCategoriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3ListCategoriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}/categories',
        http_method=u'GET',
        method_id=u'datacatalog.projects.taxonomies.categories.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha3/{+parent}/categories',
        request_field='',
        request_type_name=u'DatacatalogProjectsTaxonomiesCategoriesListRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3ListCategoriesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a category.

      Args:
        request: (DatacatalogProjectsTaxonomiesCategoriesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3Category) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}/categories/{categoriesId}',
        http_method=u'PATCH',
        method_id=u'datacatalog.projects.taxonomies.categories.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha3/{+name}',
        request_field=u'googleCloudDatacatalogV1alpha3Category',
        request_type_name=u'DatacatalogProjectsTaxonomiesCategoriesPatchRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3Category',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the IAM policy for a taxonomy or a category.

      Args:
        request: (DatacatalogProjectsTaxonomiesCategoriesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}/categories/{categoriesId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'datacatalog.projects.taxonomies.categories.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha3/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'DatacatalogProjectsTaxonomiesCategoriesSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on specified resources.

      Args:
        request: (DatacatalogProjectsTaxonomiesCategoriesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}/categories/{categoriesId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'datacatalog.projects.taxonomies.categories.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha3/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'DatacatalogProjectsTaxonomiesCategoriesTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsTaxonomiesService(base_api.BaseApiService):
    """Service class for the projects_taxonomies resource."""

    _NAME = u'projects_taxonomies'

    def __init__(self, client):
      super(DatacatalogV1alpha3.ProjectsTaxonomiesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new taxonomy in a given project.

      Args:
        request: (DatacatalogProjectsTaxonomiesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3Taxonomy) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies',
        http_method=u'POST',
        method_id=u'datacatalog.projects.taxonomies.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha3/{+parent}/taxonomies',
        request_field=u'googleCloudDatacatalogV1alpha3Taxonomy',
        request_type_name=u'DatacatalogProjectsTaxonomiesCreateRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3Taxonomy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a taxonomy. This operation will also delete all.
categories in this taxonomy.

      Args:
        request: (DatacatalogProjectsTaxonomiesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}',
        http_method=u'DELETE',
        method_id=u'datacatalog.projects.taxonomies.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha3/{+name}',
        request_field='',
        request_type_name=u'DatacatalogProjectsTaxonomiesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Export(self, request, global_params=None):
      r"""Exports all taxonomies and their categories in a project.

This method generates SerializedTaxonomy protos with nested categories that
can be used as an input for future ImportTaxonomies calls.

      Args:
        request: (DatacatalogProjectsTaxonomiesExportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3ExportTaxonomiesResponse) The response message.
      """
      config = self.GetMethodConfig('Export')
      return self._RunMethod(
          config, request, global_params=global_params)

    Export.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies:export',
        http_method=u'GET',
        method_id=u'datacatalog.projects.taxonomies.export',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'taxonomyNames'],
        relative_path=u'v1alpha3/{+parent}/taxonomies:export',
        request_field='',
        request_type_name=u'DatacatalogProjectsTaxonomiesExportRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3ExportTaxonomiesResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the taxonomy referred by name.

      Args:
        request: (DatacatalogProjectsTaxonomiesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3Taxonomy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}',
        http_method=u'GET',
        method_id=u'datacatalog.projects.taxonomies.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha3/{+name}',
        request_field='',
        request_type_name=u'DatacatalogProjectsTaxonomiesGetRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3Taxonomy',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the IAM policy for a taxonomy or a category.

      Args:
        request: (DatacatalogProjectsTaxonomiesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}:getIamPolicy',
        http_method=u'POST',
        method_id=u'datacatalog.projects.taxonomies.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha3/{+resource}:getIamPolicy',
        request_field=u'getIamPolicyRequest',
        request_type_name=u'DatacatalogProjectsTaxonomiesGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def Import(self, request, global_params=None):
      r"""Imports all taxonomies and their categories to a project as new taxonomies.

This method provides a bulk taxonomy / category creation using nested
proto structure.

      Args:
        request: (DatacatalogProjectsTaxonomiesImportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3ImportTaxonomiesResponse) The response message.
      """
      config = self.GetMethodConfig('Import')
      return self._RunMethod(
          config, request, global_params=global_params)

    Import.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies:import',
        http_method=u'POST',
        method_id=u'datacatalog.projects.taxonomies.import',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha3/{+parent}/taxonomies:import',
        request_field=u'googleCloudDatacatalogV1alpha3ImportTaxonomiesRequest',
        request_type_name=u'DatacatalogProjectsTaxonomiesImportRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3ImportTaxonomiesResponse',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all taxonomies in a project.

      Args:
        request: (DatacatalogProjectsTaxonomiesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3ListTaxonomiesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies',
        http_method=u'GET',
        method_id=u'datacatalog.projects.taxonomies.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha3/{+parent}/taxonomies',
        request_field='',
        request_type_name=u'DatacatalogProjectsTaxonomiesListRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3ListTaxonomiesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a taxonomy.

      Args:
        request: (DatacatalogProjectsTaxonomiesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudDatacatalogV1alpha3Taxonomy) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}',
        http_method=u'PATCH',
        method_id=u'datacatalog.projects.taxonomies.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha3/{+name}',
        request_field=u'googleCloudDatacatalogV1alpha3Taxonomy',
        request_type_name=u'DatacatalogProjectsTaxonomiesPatchRequest',
        response_type_name=u'GoogleCloudDatacatalogV1alpha3Taxonomy',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the IAM policy for a taxonomy or a category.

      Args:
        request: (DatacatalogProjectsTaxonomiesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'datacatalog.projects.taxonomies.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha3/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'DatacatalogProjectsTaxonomiesSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on specified resources.

      Args:
        request: (DatacatalogProjectsTaxonomiesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha3/projects/{projectsId}/taxonomies/{taxonomiesId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'datacatalog.projects.taxonomies.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha3/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'DatacatalogProjectsTaxonomiesTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(DatacatalogV1alpha3.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
