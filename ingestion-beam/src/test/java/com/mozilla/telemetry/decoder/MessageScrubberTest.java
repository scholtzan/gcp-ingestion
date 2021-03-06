/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

package com.mozilla.telemetry.decoder;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.Maps;
import com.mozilla.telemetry.util.Json;
import java.util.HashMap;
import java.util.Map;
import org.json.JSONObject;
import org.junit.Test;

public class MessageScrubberTest {

  @Test
  public void testShouldScrubBug1567596() throws Exception {
    Map<String, String> attributes = ImmutableMap.<String, String>builder()
        .put(ParseUri.DOCUMENT_NAMESPACE, "telemetry").put(ParseUri.DOCUMENT_TYPE, "crash")
        .put(ParseUri.APP_UPDATE_CHANNEL, "nightly").put(ParseUri.APP_BUILD_ID, "20190719094503")
        .put(ParseUri.APP_VERSION, "70.0a1").build();
    JSONObject bug1567596AffectedJson = Json.readJSONObject(("{\n" //
        + "  \"payload\": {\n" //
        + "    \"metadata\": {\n" //
        + "      \"MozCrashReason\": \"bar; do not use eval with system privileges foo)\"\n" //
        + "    },\n" //
        + "    \"session_id\": \"ca98fe03-1248-448f-bbdf-59f97dba5a0e\"\n" //
        + "  },\n" //
        + "  \"client_id\": null\n" + "}").getBytes());
    assertTrue(MessageScrubber.shouldScrub(attributes, bug1567596AffectedJson));
    assertFalse(MessageScrubber.shouldScrub(new HashMap<>(), bug1567596AffectedJson));
    assertFalse(MessageScrubber.shouldScrub(attributes, new JSONObject()));
  }

  @Test
  public void testShouldScrubCrashBug1562011() throws Exception {
    JSONObject ping = Json.readJSONObject(("{\n" //
        + "  \"payload\": {\n" //
        + "    \"metadata\": {\n" //
        + "      \"RemoteType\": \"webIsolated=foo\"\n" //
        + "    },\n" //
        + "    \"session_id\": \"ca98fe03-1248-448f-bbdf-59f97dba5a0e\"\n" //
        + "  },\n" //
        + "  \"client_id\": null\n" + "}").getBytes());

    Map<String, String> attributes = Maps.newHashMap(ImmutableMap.<String, String>builder()
        .put(ParseUri.DOCUMENT_NAMESPACE, "telemetry").put(ParseUri.DOCUMENT_TYPE, "crash")
        .put(ParseUri.APP_UPDATE_CHANNEL, "nightly").put(ParseUri.APP_VERSION, "68.0").build());

    assertTrue(MessageScrubber.shouldScrub(attributes, ping));

    attributes.put(ParseUri.APP_UPDATE_CHANNEL, "beta");
    attributes.put(ParseUri.APP_VERSION, "68");
    assertTrue(MessageScrubber.shouldScrub(attributes, ping));

    attributes.put(ParseUri.APP_VERSION, "69");
    assertFalse(MessageScrubber.shouldScrub(attributes, ping));
  }

  @Test
  public void testShouldScrubBhrBug1562011() throws Exception {
    JSONObject ping = Json.readJSONObject(("{\n" //
        + "  \"payload\": {\n" //
        + "    \"hangs\": [\n" //
        + "      {\"remoteType\": \"webIsolated=foo\"},\n" //
        + "      {\"remoteType\": \"web\"}\n" //
        + "    ],\n" //
        + "    \"session_id\": \"ca98fe03-1248-448f-bbdf-59f97dba5a0e\"\n" //
        + "  },\n" //
        + "  \"client_id\": null\n" + "}").getBytes());

    Map<String, String> attributes = ImmutableMap.<String, String>builder()
        .put(ParseUri.DOCUMENT_NAMESPACE, "telemetry").put(ParseUri.DOCUMENT_TYPE, "bhr")
        .put(ParseUri.APP_UPDATE_CHANNEL, "nightly").put(ParseUri.APP_VERSION, "68.0").build();

    assertTrue(MessageScrubber.shouldScrub(attributes, ping));
  }

}
