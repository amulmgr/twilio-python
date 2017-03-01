# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio import serialize
from twilio import values
from twilio.instance_context import InstanceContext
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page


class WorkerStatisticsList(ListResource):

    def __init__(self, version, workspace_sid, worker_sid):
        """
        Initialize the WorkerStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param worker_sid: The worker_sid

        :returns: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsList
        :rtype: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsList
        """
        super(WorkerStatisticsList, self).__init__(version)

        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
            'worker_sid': worker_sid,
        }

    def get(self):
        """
        Constructs a WorkerStatisticsContext

        :returns: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsContext
        """
        return WorkerStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            worker_sid=self._solution['worker_sid'],
        )

    def __call__(self):
        """
        Constructs a WorkerStatisticsContext

        :returns: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsContext
        """
        return WorkerStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            worker_sid=self._solution['worker_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkerStatisticsList>'


class WorkerStatisticsPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the WorkerStatisticsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid
        :param worker_sid: The worker_sid

        :returns: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsPage
        :rtype: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsPage
        """
        super(WorkerStatisticsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkerStatisticsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsInstance
        """
        return WorkerStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            worker_sid=self._solution['worker_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkerStatisticsPage>'


class WorkerStatisticsContext(InstanceContext):

    def __init__(self, version, workspace_sid, worker_sid):
        """
        Initialize the WorkerStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param worker_sid: The worker_sid

        :returns: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsContext
        """
        super(WorkerStatisticsContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
            'worker_sid': worker_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workers/{worker_sid}/Statistics'.format(**self._solution)

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset):
        """
        Fetch a WorkerStatisticsInstance

        :param unicode minutes: The minutes
        :param datetime start_date: The start_date
        :param datetime end_date: The end_date

        :returns: Fetched WorkerStatisticsInstance
        :rtype: twilio.rest.taskrouter.twilio.com.v1.worker_statistics.WorkerStatisticsList
        """
        params = values.of({
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'EndDate': serialize.iso8601_datetime(end_date),
        })

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return WorkerStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            worker_sid=self._solution['worker_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkerStatisticsContext {}>'.format(context)


class WorkerStatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, worker_sid):
        """
        Initialize the WorkerStatisticsInstance

        :returns: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsInstance
        """
        super(WorkerStatisticsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'cumulative': payload['cumulative'],
            'worker_sid': payload['worker_sid'],
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid,
            'worker_sid': worker_sid,
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: WorkerStatisticsContext for this WorkerStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.worker_statistics.WorkerStatisticsContext
        """
        if self._context is None:
            self._context = WorkerStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                worker_sid=self._solution['worker_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def cumulative(self):
        """
        :returns: The cumulative
        :rtype: dict
        """
        return self._properties['cumulative']

    @property
    def worker_sid(self):
        """
        :returns: The worker_sid
        :rtype: unicode
        """
        return self._properties['worker_sid']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset):
        """
        Fetch a WorkerStatisticsInstance

        :param unicode minutes: The minutes
        :param datetime start_date: The start_date
        :param datetime end_date: The end_date

        :returns: Fetched WorkerStatisticsInstance
        :rtype: twilio.rest.taskrouter.twilio.com.v1.worker_statistics.WorkerStatisticsList
        """
        return self._proxy.fetch(
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkerStatisticsInstance {}>'.format(context)
