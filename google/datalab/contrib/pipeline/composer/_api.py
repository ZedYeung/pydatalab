# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.

"""Implements Composer HTTP API wrapper."""
import google.datalab.utils


class Api(object):
  """A helper class to issue Composer HTTP requests."""

  _ENDPOINT = 'https://composer.googleapis.com/v1alpha1'
  _ENVIRONMENTS_PATH = '/projects/%s/locations/%s/environments/%s'

  _DEFAULT_TIMEOUT = 60000

  def environment_details_get(self, zone, environment):
    """ Issues a request to load data from GCS to a BQ table

    Args:
      zone: GCP zone of the composer environment
      environment: name of the Composer environment
    Returns:
      A parsed result object.
    Raises:
      Exception if there is an error performing the operation.
    """
    default_context = google.datalab.Context.default()
    url = Api._ENDPOINT + (Api._ENVIRONMENTS_PATH % (default_context.project_id, zone, environment))

    args = {
        'timeoutMs': Api._DEFAULT_TIMEOUT,
    }

    return google.datalab.utils.Http.request(url, args=args,
                                             credentials=default_context.credentials)
