config = {
  "interfaces": {
    "google.cloud.datacatalog.v1beta1.PolicyTagManagerSerialization": {
      "retry_codes": {
        "idempotent": [
          "DEADLINE_EXCEEDED",
          "UNAVAILABLE"
        ],
        "non_idempotent": []
      },
      "retry_params": {
        "default": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 20000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 20000,
          "total_timeout_millis": 600000
        }
      },
      "methods": {
        "ImportTaxonomies": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "ExportTaxonomies": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        }
      }
    }
  }
}
