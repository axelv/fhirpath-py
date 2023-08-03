import fhirpathpy.engine.invocations.collections as collections
import fhirpathpy.engine.invocations.existence as existence
import fhirpathpy.engine.invocations.filtering as filtering
import fhirpathpy.engine.invocations.subsetting as subsetting
import fhirpathpy.engine.invocations.strings as strings
import fhirpathpy.engine.invocations.navigation as navigation
import fhirpathpy.engine.invocations.combining as combining
import fhirpathpy.engine.invocations.math as math
import fhirpathpy.engine.invocations.misc as misc
import fhirpathpy.engine.invocations.equality as equality
import fhirpathpy.engine.invocations.logic as logic
import fhirpathpy.engine.invocations.datetime as datetime

invocations = {
    "empty": {"fn": existence.empty_fn},
    "not": {"fn": existence.not_fn},
    "exists": {"fn": existence.exists_macro, "arity": {0: [], 1: ["Expr"]}},
    "all": {"fn": existence.all_macro, "arity": {1: ["Expr"]}},
    "allTrue": {"fn": existence.all_true_fn},
    "anyTrue": {"fn": existence.any_true_fn},
    "allFalse": {"fn": existence.all_false_fn},
    "anyFalse": {"fn": existence.any_false_fn},
    "subsetOf": {"fn": existence.subset_of_fn, "arity": {1: ["AnyAtRoot"]}},
    "supersetOf": {"fn": existence.superset_of_fn, "arity": {1: ["AnyAtRoot"]}},
    "isDistinct": {"fn": existence.isdistinct_fn},
    "distinct": {"fn": existence.distinct_fn},
    "count": {"fn": existence.count_fn},
    "repeat": {"fn": filtering.repeat_macro, "arity": {1: ["Expr"]}},
    "where": {"fn": filtering.where_macro, "arity": {1: ["Expr"]}},
    "extension": {"fn": filtering.extension, "arity": {1: ["String"]}},
    "select": {"fn": filtering.select_macro, "arity": {1: ["Expr"]}},
    "single": {"fn": filtering.single_fn},
    "first": {"fn": filtering.first_fn},
    "last": {"fn": filtering.last_fn},
    "ofType": {"fn": filtering.of_type_fn, "arity": {1: ["Identifier"]}},
    "tail": {"fn": filtering.tail_fn},
    "take": {"fn": filtering.take_fn, "arity": {1: ["Integer"]}},
    "skip": {"fn": filtering.skip_fn, "arity": {1: ["Integer"]}},
    "intersect": {"fn": subsetting.intersect_fn, "arity": {1: ["AnyAtRoot"]}},
    "combine": {"fn": combining.combine_fn, "arity": {1: ["AnyAtRoot"]}},
    "iif": {"fn": misc.iif_macro, "arity": {2: ["Expr", "Expr"], 3: ["Expr", "Expr", "Expr"]}},
    "trace": {"fn": misc.trace_fn, "arity": {0: [], 1: ["String"]}},
    "toInteger": {"fn": misc.to_integer},
    "toDecimal": {"fn": misc.to_decimal},
    "toString": {"fn": misc.to_string},
    "toDateTime": {"fn": misc.to_date_time},
    "toTime": {"fn": misc.to_time},
    "indexOf": {"fn": strings.index_of, "arity": {1: ["String"]}, "nullable_input": True},
    "substring": {
        "fn": strings.substring,
        "arity": {1: ["Integer"], 2: ["Integer", "Integer"]},
        "nullable_input": True,
    },
    "startsWith": {"fn": strings.starts_with, "arity": {1: ["String"]}, "nullable_input": True},
    "endsWith": {"fn": strings.ends_with, "arity": {1: ["String"]}, "nullable_input": True},
    "contains": {"fn": strings.contains_fn, "arity": {1: ["String"]}, "nullable_input": True},
    "replace": {"fn": strings.replace, "arity": {2: ["String", "String"]}, "nullable_input": True},
    "matches": {"fn": strings.matches, "arity": {1: ["String"]}, "nullable_input": True},
    "replaceMatches": {
        "fn": strings.replace_matches,
        "arity": {2: ["String", "String"]},
        "nullable_input": True,
    },
    "length": {"fn": strings.length, "nullable_input": True},
    "abs": {"fn": math.abs},
    "ceiling": {"fn": math.ceiling},
    "exp": {"fn": math.exp},
    "floor": {"fn": math.floor},
    "ln": {"fn": math.ln},
    "log": {"fn": math.log, "arity": {1: ["Number"]}, "nullable": True},
    "power": {"fn": math.power, "arity": {1: ["Number"]}, "nullable": True},
    "round": {"fn": math.rround, "arity": {1: ["Number"]}},
    "sqrt": {"fn": math.sqrt},
    "truncate": {"fn": math.truncate},
    "now": {"fn": datetime.now},
    "today": {"fn": datetime.today},
    "timeOfDay": {"fn": datetime.timeOfDay},
    "children": {"fn": navigation.children},
    "descendants": {"fn": navigation.descendants},
    "|": {"fn": combining.union_op, "arity": {2: ["Any", "Any"]}},
    "=": {"fn": equality.equal, "arity": {2: ["Any", "Any"]}, "nullable": True},
    "!=": {"fn": equality.unequal, "arity": {2: ["Any", "Any"]}, "nullable": True},
    "~": {"fn": equality.equival, "arity": {2: ["Any", "Any"]}},
    "!~": {"fn": equality.unequival, "arity": {2: ["Any", "Any"]}},
    "<": {"fn": equality.lt, "arity": {2: ["Any", "Any"]}, "nullable": True},
    ">": {"fn": equality.gt, "arity": {2: ["Any", "Any"]}, "nullable": True},
    "<=": {"fn": equality.lte, "arity": {2: ["Any", "Any"]}, "nullable": True},
    ">=": {"fn": equality.gte, "arity": {2: ["Any", "Any"]}, "nullable": True},
    "containsOp": {"fn": collections.contains, "arity": {2: ["Any", "Any"]}},
    "inOp": {"fn": collections.inn, "arity": {2: ["Any", "Any"]}},
    "&": {"fn": math.amp, "arity": {2: ["String", "String"]}},
    "+": {"fn": math.plus, "arity": {2: ["Any", "Any"]}, "nullable": True},
    "-": {"fn": math.minus, "arity": {2: ["Any", "Any"]}, "nullable": True},
    "*": {"fn": math.mul, "arity": {2: ["Number", "Number"]}, "nullable": True},
    "/": {"fn": math.div, "arity": {2: ["Number", "Number"]}, "nullable": True},
    "mod": {"fn": math.mod, "arity": {2: ["Number", "Number"]}, "nullable": True},
    "div": {"fn": math.intdiv, "arity": {2: ["Number", "Number"]}, "nullable": True},
    "or": {"fn": logic.or_op, "arity": {2: [["Boolean"], ["Boolean"]]}},
    "and": {"fn": logic.and_op, "arity": {2: [["Boolean"], ["Boolean"]]}},
    "xor": {"fn": logic.xor_op, "arity": {2: [["Boolean"], ["Boolean"]]}},
    "implies": {"fn": logic.implies_op, "arity": {2: [["Boolean"], ["Boolean"]]}},
}
